# onos-docker SDN mininet OpenFlow wireshark

----

- [ONOS-Docker](https://onosproject.org)  
- [Mininet](http://mininet.org/)

- At leasts 4GB of memory
- At least 2 cpu cores  
- At least 20GB of space  

Ports:
ONOS requires the following ports to be open, in order to make the corresponding functionalities available:  
- 8181    for REST API and GUI  
- 8101    to access the ONOS CLI  
- 9876    for intra-cluster communication (communication between target machines)  
- 6653    optional, for OpenFlow  
- 6640    optional, for OVSDB  


[Requirements](https://wiki.onosproject.org/display/ONOS/Requirement)

```
vagrant up gateway01  
vagrant ssh gateway01
```

```
vagrant@gateway01:~$ hostnamectl
   Static hostname: gateway01
         Icon name: computer-vm
           Chassis: vm
        Machine ID: b4d34378b21de2b163f4308a5c266ccb
           Boot ID: 92fc28147d4a48ce927e83e5c4de3e8c
    Virtualization: oracle
  Operating System: Ubuntu 16.04.5 LTS
            Kernel: Linux 4.4.0-131-generic
      Architecture: x86-64
vagrant@gateway01:~$ ifconfig
      docker0   Link encap:Ethernet  HWaddr 02:42:9a:14:81:e6
                inet addr:172.17.0.1  Bcast:172.17.255.255  Mask:255.255.0.0
                inet6 addr: fe80::42:9aff:fe14:81e6/64 Scope:Link
                UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
                RX packets:4063 errors:0 dropped:0 overruns:0 frame:0
                TX packets:3967 errors:0 dropped:0 overruns:0 carrier:0
                collisions:0 txqueuelen:0
                RX bytes:3541118 (3.5 MB)  TX bytes:1769004 (1.7 MB)

      eth0      Link encap:Ethernet  HWaddr 08:00:27:ee:87:c4
                inet addr:10.0.2.15  Bcast:10.0.2.255  Mask:255.255.255.0
                inet6 addr: fe80::a00:27ff:feee:87c4/64 Scope:Link
                UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
                RX packets:486419 errors:0 dropped:0 overruns:0 frame:0
                TX packets:70086 errors:0 dropped:0 overruns:0 carrier:0
                collisions:0 txqueuelen:1000
                RX bytes:633875963 (633.8 MB)  TX bytes:4529749 (4.5 MB)

      eth1      Link encap:Ethernet  HWaddr 08:00:27:a4:9a:ba
                inet addr:192.168.45.11  Bcast:192.168.45.255  Mask:255.255.255.0
                inet6 addr: fe80::a00:27ff:fea4:9aba/64 Scope:Link
                UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
                RX packets:1803 errors:0 dropped:0 overruns:0 frame:0
                TX packets:2897 errors:0 dropped:0 overruns:0 carrier:0
                collisions:0 txqueuelen:1000
                RX bytes:209746 (209.7 KB)  TX bytes:5429578 (5.4 MB)

      lo        Link encap:Local Loopback
                inet addr:127.0.0.1  Mask:255.0.0.0
                inet6 addr: ::1/128 Scope:Host
                UP LOOPBACK RUNNING  MTU:65536  Metric:1
                RX packets:0 errors:0 dropped:0 overruns:0 frame:0
                TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
                collisions:0 txqueuelen:1
                RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)

      vethd3208d6 Link encap:Ethernet  HWaddr 52:69:30:3f:e7:76
                inet6 addr: fe80::5069:30ff:fe3f:e776/64 Scope:Link
                UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
                RX packets:4063 errors:0 dropped:0 overruns:0 frame:0
                TX packets:3975 errors:0 dropped:0 overruns:0 carrier:0
                collisions:0 txqueuelen:0
                RX bytes:3598000 (3.5 MB)  TX bytes:1769652 (1.7 MB)
```

```
username/password : onos/rocks

menu - applications - activate  
Reactive Forwarding  
OpenFlow Provider Suite  

menu - topology - left bottom pull-push menu
toggle host visibility

onos GUI : http://192.168.45.11:8181/onos/ui/

```
```
ONOS Core REST API
http://192.168.45.11:8181/onos/v1/docs
```

```
sudo docker container ls
sudo docker exec -it <CONTAINERID> bash

https://hub.docker.com/r/onosproject/onos/
```

```
vagrant@gateway01:~$ sudo docker container ls
CONTAINER ID        IMAGE                    COMMAND                  CREATED              STATUS              PORTS                                                            NAMES
b7a0d48675d0        onosproject/onos:2.1.0   "./bin/onos-service …"   About a minute ago   Up About a minute   6640/tcp, 6653/tcp, 8101/tcp, 9876/tcp, 0.0.0.0:8181->8181/tcp   simple-onos
```

```
recommended options:
-n: install core Mininet dependencies;
-v: install Open vSwitch;
-f: install legacy Stanford 1.0 user switch and controller;
-w: install wireshark and improved OpenFlow wireshark dissector)

git clone http://github.com/mininet/mininet
mininet/util/install.sh -nvfw
Wireshark version 2.6.8 >= 1.12 - returning
```


```
vagrant@gateway01:~$ sudo docker inspect b7a0d48675d0 | grep IPAddress
            "SecondaryIPAddresses": null,
            "IPAddress": "172.17.0.2",
                    "IPAddress": "172.17.0.2",
```

```
vagrant@gateway01:~$ sudo mn --controller remote,ip=172.17.0.2
vagrant@gateway01:~$ sudo mn -c
*** Cleanup complete.
```

```
# default port 6633
sudo mn --controller remote,ip=172.17.0.2

sudo mn --controller=remote,ip=172.17.0.2,port=6633 --mac --topo=tree,2,2 --switch=ovsk,protocols=OpenFlow13

sudo mn --controller=remote,ip=172.17.0.2,port=6633  --topo=linear,4
sudo mn --controller=remote,ip=172.17.0.2,port=6633  --topo=linear,20
# create a linear topology of 200 switches
sudo mn --controller=remote,ip=172.17.0.2,port=6633  --topo=linear,200

# create  a single switch with 4 hosts
sudo mn --controller=remote,ip=172.17.0.2,port=6633 --topo=single,4
sudo mn --controller=remote,ip=172.17.0.2,port=6633 --topo=single,96


# A tree topology has a single switch with others connected to it based on a fanout number.
# A fanout value of 3 means 3 switches are connected to the core switch and each of those switches potentially has 3 switches connected to it.
# The fanout also determines the number of hosts connected to each leaf/edge switch.
sudo mn --controller=remote,ip=172.17.0.2,port=6633 --topo=tree,depth=3,fanout=3
sudo mn --controller=remote,ip=172.17.0.2,port=6633 --topo=tree,depth=3,fanout=4
sudo mn --controller=remote,ip=172.17.0.2,port=6633 --topo=tree,depth=2,fanout=10
sudo mn --controller=remote,ip=172.17.0.2,port=6633 --topo=tree,depth=5,fanout=3

sudo mn --controller=remote,ip=172.17.0.2,port=6633 --topo=torus,3,3
sudo mn --controller=remote,ip=172.17.0.2,port=6633 --topo=torus,4,4
```

```
sudo mn --test iperf --topo single,3 --controller remote,ip=172.17.0.2
sudo mn --test pingall --topo single,3 --controller remote,ip=172.17.0.2
sudo mn --test pingall --topo single,3 --controller remote,ip=172.17.0.2 -v debug
```

Custom Topology
```
$ sudo mn --custom /vagrant/topologies/simple.py --controller remote,ip=172.17.0.2,port=6633
mininet> pingall
onos GUI - Topology

```

```
$ sudo python /vagrant/topologies/simple1.py
mininet> pingall
onos GUI - Topology

OR

sudo mn --custom /vagrant/topologies/simple1.py --topo minimal --controller remote,ip=172.17.0.2
mininet> pingall
onos GUI - Topology
```

```
simple1 a single switch and three hosts
simple2 two switches two hosts
simple3 k: number of switches n: number of hosts per switch
simple4 WAN Topology

```
