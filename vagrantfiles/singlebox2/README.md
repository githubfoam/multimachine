# sandboxes

run first shell script
~~~~
$script = <<SCRIPT
~~~~

~~~~
vagrant up
vagrant ssh
vagrant destroy
~~~~
~~~~
config.vm.network "private_network", ip: "192.168.45.10"  
config.vm.network "forwarded_port", guest: 80, host: 80  

$ hostnamectl
   Static hostname: terraform-sandbox
         Icon name: computer-vm
           Chassis: vm
        Machine ID: 769489ce92bb45a19917d38d72c6c8f8
           Boot ID: 6d7ba7649da544ce8e8a9f54d7631590
    Virtualization: oracle
  Operating System: Ubuntu 18.04.1 LTS
            Kernel: Linux 4.15.0-29-generic
      Architecture: x86-64

$ ifconfig
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.0.2.15  netmask 255.255.255.0  broadcast 10.0.2.255
        inet6 fe80::a00:27ff:fec2:be11  prefixlen 64  scopeid 0x20<link>
        ether 08:00:27:c2:be:11  txqueuelen 1000  (Ethernet)
        RX packets 9592  bytes 7418929 (7.4 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 4596  bytes 399224 (399.2 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.45.10  netmask 255.255.255.0  broadcast 192.168.45.255
        inet6 fe80::a00:27ff:fe6f:38bf  prefixlen 64  scopeid 0x20<link>
        ether 08:00:27:6f:38:bf  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 12  bytes 936 (936.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 28  bytes 2482 (2.4 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 28  bytes 2482 (2.4 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
~~~~
