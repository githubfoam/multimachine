# onos SDN mininet OpenFlow

----

- [ONOS](https://onosproject.org)  
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
vagrant up onos01  
vagrant ssh onos01
```

```
$ hostnamectl
   Static hostname: onos01
         Icon name: computer-vm
           Chassis: vm
        Machine ID: fa8a1edd06864f47ba4cad5d0f5ca134
           Boot ID: 084d3e7bd2c1463f939d55f094c95e05
    Virtualization: oracle
  Operating System: Fedora 29 (Twenty Nine)
       CPE OS Name: cpe:/o:fedoraproject:fedora:29
            Kernel: Linux 4.18.16-300.fc29.x86_64
      Architecture: x86-64
      $ ifconfig
      enp0s3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
              inet 10.0.2.15  netmask 255.255.255.0  broadcast 10.0.2.255
              inet6 fe80::251d:4ecb:b5fa:b3b6  prefixlen 64  scopeid 0x20<link>
              ether 08:00:27:77:d2:06  txqueuelen 1000  (Ethernet)
              RX packets 466219  bytes 599998184 (572.2 MiB)
              RX errors 0  dropped 0  overruns 0  frame 0
              TX packets 164345  bytes 16519431 (15.7 MiB)
              TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

      enp0s8: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
              inet 192.168.45.10  netmask 255.255.255.0  broadcast 192.168.45.255
              inet6 fe80::a00:27ff:fe51:6382  prefixlen 64  scopeid 0x20<link>
              ether 08:00:27:51:63:82  txqueuelen 1000  (Ethernet)
              RX packets 521  bytes 53184 (51.9 KiB)
              RX errors 0  dropped 0  overruns 0  frame 0
              TX packets 888  bytes 1438644 (1.3 MiB)
              TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

      lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
              inet 127.0.0.1  netmask 255.0.0.0
              inet6 ::1  prefixlen 128  scopeid 0x10<host>
              loop  txqueuelen 1000  (Local Loopback)
              RX packets 102  bytes 7768 (7.5 KiB)
              RX errors 0  dropped 0  overruns 0  frame 0
              TX packets 102  bytes 7768 (7.5 KiB)
              TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

```
username/password : onos/rocks

menu - applications - activate  
Reactive Forwarding  
OpenFlow Provider Suite  

menu - topology - left bottom pull-push menu
toggle host visibility

onos GUI : http://192.168.45.10:8181/onos/ui/

ONOS Core REST API
http://192.168.45.10:8181/onos/v1/docs

ONOS Controller IP : 192.168.45.10

mininet experimental

```
```


$ sudo /opt/onos/bin/onos -l onos
Password authentication
Password:
Welcome to Open Network Operating System (ONOS)!
     ____  _  ______  ____
    / __ \/ |/ / __ \/ __/
   / /_/ /    / /_/ /\ \
   \____/_/|_/\____/___/

Documentation: wiki.onosproject.org
Tutorials:     tutorials.onosproject.org
Mailing lists: lists.onosproject.org

Come help out! Find out how at: contribute.onosproject.org

Hit '<tab>' for a list of available commands
and '[cmd] --help' for help on a specific command.
Hit '<ctrl-d>' or type 'logout' to exit ONOS session.
```
