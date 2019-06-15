# onos SDN OpenFlow

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
        Machine ID: cfa0388701ff415dbceb1d083ec3fdfd
           Boot ID: 0a703c473c6d4c25ba3217900de5c890
    Virtualization: kvm
  Operating System: CentOS Linux 7 (Core)
       CPE OS Name: cpe:/o:centos:centos:7
            Kernel: Linux 3.10.0-957.1.3.el7.x86_64
      Architecture: x86-64
$ ifconfig
eth0      Link encap:Ethernet  HWaddr 08:00:27:ee:87:c4
          inet addr:10.0.2.15  Bcast:10.0.2.255  Mask:255.255.255.0
          inet6 addr: fe80::a00:27ff:feee:87c4/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:112595 errors:0 dropped:0 overruns:0 frame:0
          TX packets:56932 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:81286389 (81.2 MB)  TX bytes:5045282 (5.0 MB)

eth1      Link encap:Ethernet  HWaddr 08:00:27:c2:c1:34
          inet addr:192.168.45.10  Bcast:192.168.45.255  Mask:255.255.255.0
          inet6 addr: fe80::a00:27ff:fec2:c134/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:12524 errors:0 dropped:0 overruns:0 frame:0
          TX packets:19357 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:2020998 (2.0 MB)  TX bytes:39167944 (39.1 MB)

lo        Link encap:Local Loopback
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:1587 errors:0 dropped:0 overruns:0 frame:0
          TX packets:1587 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1
          RX bytes:108090 (108.0 KB)  TX bytes:108090 (108.0 KB)
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
