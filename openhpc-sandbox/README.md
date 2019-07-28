# OpenHPC Sandbox


nodes
~~~~
master01
compute01
compute02
~~~~

~~~~
installer user: vagrant
passwordless ssh between all nodes
fakenfs: shared RPMS dir
~~~~

~~~~
ROOT MUST BE (not vagrant)

# initialize PBS path
. /etc/profile.d/pbs.sh
# enable user environment propagation (needed for modules support)
qmgr -c "set server default_qsub_arguments= -V"
# enable uniform multi-node MPI task distribution
qmgr -c "set server resources_default.place=scatter"
# enable support for job accounting
qmgr -c "set server job_history_enable=True"
# register compute hosts with pbspro

~~~~

~~~~
[vagrant@master01 groups.d]$ wwsh file list
dynamic_hosts           :  rw-r--r-- 0   root root              688 /etc/hosts
group                   :  rw-r--r-- 1   root root              679 /etc/group
network                 :  rw-r--r-- 1   root vagrant            16 /etc/sysconfig/network
passwd                  :  rw-r--r-- 1   root root             1590 /etc/passwd
shadow                  :  rw-r----- 1   root root              983 /etc/shadow
[vagrant@master01 groups.d]$ wwsh node list
NAME                GROUPS              IPADDR              HWADDR
================================================================================
compute01           UNDEF               192.168.1.253       08:00:27:e3:b0:01
compute02           UNDEF               192.168.1.252       08:00:27:77:86:f5
[vagrant@master01 groups.d]$ sudo wwsh provision list
NODE                VNFS            BOOTSTRAP             FILES
================================================================================
compute01           centos7.6       3.10.0-957.1.3.el7... dynamic_hosts,grou...
compute02           centos7.6       3.10.0-957.1.3.el7... dynamic_hosts,grou...

[vagrant@master01 ~]$ pdsh -w compute0[1-2] uptime
compute01:  13:42:52 up 23 min,  0 users,  load average: 0.00, 0.01, 0.03
compute02:  13:42:52 up  3:25,  2 users,  load average: 0.00, 0.01, 0.05


[vagrant@master01 ~]$ wwsh vnfs list
VNFS NAME            SIZE (M)   ARCH       CHROOT LOCATION
centos7.6            279.8      x86_64     /opt/ohpc/admin/images/centos7.6

[vagrant@master01 ~]$ pbsnodes -a
compute01
     Mom = compute01.localdomain
     ntype = PBS
     state = state-unknown,down
     pcpus = 1
     resources_available.host = compute01
     resources_available.ncpus = 1
     resources_available.vnode = compute01
     resources_assigned.accelerator_memory = 0kb
     resources_assigned.hbmem = 0kb
     resources_assigned.mem = 0kb
     resources_assigned.naccelerators = 0
     resources_assigned.ncpus = 0
     resources_assigned.vmem = 0kb
     comment = node down: communication closed
     resv_enable = True
     sharing = default_shared
     last_state_change_time = Sun Jul 28 11:40:41 2019

compute02
     Mom = compute02
     ntype = PBS
     state = state-unknown,down
     pcpus = 1
     resources_available.host = compute02
     resources_available.ncpus = 1
     resources_available.vnode = compute02
     resources_assigned.accelerator_memory = 0kb
     resources_assigned.hbmem = 0kb
     resources_assigned.mem = 0kb
     resources_assigned.naccelerators = 0
     resources_assigned.ncpus = 0
     resources_assigned.vmem = 0kb
     comment = node down: communication closed
     resv_enable = True
     sharing = default_shared
     last_state_change_time = Sun Jul 28 11:40:41 2019

~~~~
OpenHPC 1.3.8
~~~~
Install guide with Warewulf + PBS Professional (PDF)
https://github.com/openhpc/ohpc/releases/download/v1.3.8.GA/Install_guide-CentOS7-Warewulf-PBSPro-1.3.8-x86_64.pdf
~~~~
