# -*- mode: ruby -*-
# vi: set ft=ruby :


Vagrant.configure("2") do |config|
  config.vm.provider "virtualbox" do |vb|
    vb.gui = false
    vb.memory = "512"
    vb.cpus = 2
  end

  config.vm.define "master01" do |hpcluster|
    hpcluster.vm.box = "bento/centos-7.6"
    hpcluster.vm.hostname = "master01"
    hpcluster.vm.network "private_network", ip: "192.168.1.254"
    hpcluster.vm.provider "virtualbox" do |vb|
        vb.name = "master01"
        vb.memory = "1024"
    end
    hpcluster.vm.provision "ansible_local" do |ansible|
    ansible.playbook = "deploy.yml"
    ansible.become = true
    ansible.compatibility_mode = "2.0"
    ansible.version = "2.8.2"
    end
    hpcluster.vm.provision "shell", inline: <<-SHELL
    systemctl disable firewalld
    systemctl stop firewalld
    yum -y update
    yum install -y wget
    # yum install -y https://github.com/openhpc/ohpc/releases/download/v1.3.GA/ohpc-release-1.3-1.el7.x86_64.rpm
    # yum install -y ohpc-base ohpc-warewulf
    # systemctl enable ntpd.service
    # echo "server tr.pool.ntp.org" | sudo tee -a /etc/ntp.conf
    # systemctl restart ntpd
    # yum install -y pbspro-server-ohpc
    # DOES NOT WORK !!!
    # perl -pi -e "s/^\s+disable\s+= yes/ disable = no/" /etc/xinetd.d/tftp
    # systemctl restart xinetd
    # systemctl enable --now mariadb.service
    # systemctl enable --now httpd.service
    # systemctl enable dhcpd.service
    # export CHROOT=/opt/ohpc/admin/images/centos7.6
    # wwmkchroot centos-7 $CHROOT
    # yum -y --installroot=$CHROOT install ohpc-base-compute
    # yum -y --installroot=$CHROOT install pbspro-execution-ohpc
    # yum -y --installroot=$CHROOT install pbspro-execution-ohpc
    # perl -pi -e "s/PBS_SERVER=\S+/PBS_SERVER=master01/" $CHROOT/etc/pbs.conf
    # perl -pi -e "s/\$clienthost \S+/\$clienthost master01/" $CHROOT/var/spool/pbs/mom_priv/config
    # chroot $CHROOT opt/pbs/libexec/pbs_habitat
    # echo "\$usecp *:/home /home" | sudo tee -a $CHROOT/var/spool/pbs/mom_priv/config
    # perl -pi -e "s/\$clienthost \S+/\$clienthost master01/" $CHROOT/var/spool/pbs/mom_priv/config
    # chroot $CHROOT systemctl enable pbs
    # yum -y --installroot=$CHROOT install ntp
    # yum -y --installroot=$CHROOT install kernel
    # yum -y --installroot=$CHROOT install lmod-ohpc
    # wwinit database
    # wwinit ssh_keys
    # echo "192.168.1.254:/home /home nfs nfsvers=3,nodev,nosuid 0 0" | sudo tee -a $CHROOT/etc/fstab
    # echo "192.168.1.254:/opt/ohpc/pub /opt/ohpc/pub nfs nfsvers=3,nodev 0 0" | sudo tee -a $CHROOT/etc/fstab
    # echo "/home *(rw,no_subtree_check,fsid=10,no_root_squash)" | sudo tee -a /etc/exports
    # echo "/opt/ohpc/pub *(ro,no_subtree_check,fsid=11)" | sudo tee -a /etc/exports
    # systemctl restart nfs-server
    # systemctl enable nfs-server
    # chroot $CHROOT systemctl enable ntpd
    # echo "server 192.168.1.254" | sudo tee -a $CHROOT/etc/ntp.conf
    # perl -pi -e 's/# End of file/\* soft memlock unlimited\n$&/s' /etc/security/limits.conf
    # perl -pi -e 's/# End of file/\* hard memlock unlimited\n$&/s' /etc/security/limits.conf
    # perl -pi -e 's/# End of file/\* soft memlock unlimited\n$&/s' $CHROOT/etc/security/limits.conf
    # perl -pi -e 's/# End of file/\* hard memlock unlimited\n$&/s' $CHROOT/etc/security/limits.conf
    # # Configure SMS to receive messages and reload rsyslog configuration
    # perl -pi -e "s/\\#\\\$ModLoad imudp/\\\$ModLoad imudp/" /etc/rsyslog.conf
    # perl -pi -e "s/\\#\\\$UDPServerRun 514/\\\$UDPServerRun 514/" /etc/rsyslog.conf
    # systemctl restart rsyslog
    # # Define compute node forwarding destination
    # echo "*.* @192.168.1.254:514" | sudo tee -a $CHROOT/etc/rsyslog.conf
    # # Disable most local logging on computes. Emergency and boot logs will remain on the compute nodes
    # perl -pi -e "s/^\*\.info/\\#\*\.info/" $CHROOT/etc/rsyslog.conf
    # perl -pi -e "s/^authpriv/\\#authpriv/" $CHROOT/etc/rsyslog.conf
    # perl -pi -e "s/^mail/\\#mail/" $CHROOT/etc/rsyslog.conf
    # perl -pi -e "s/^cron/\\#cron/" $CHROOT/etc/rsyslog.conf
    # perl -pi -e "s/^uucp/\\#uucp/" $CHROOT/etc/rsyslog.conf
    # # Install Ganglia meta-package on master
    # yum -y install ohpc-ganglia
    # # Install Ganglia compute node daemon
    # yum -y --installroot=$CHROOT install ganglia-gmond-ohpc
    # # Use example configuration script to enable unicast receiver on master host
    # cp /opt/ohpc/pub/examples/ganglia/gmond.conf /etc/ganglia/gmond.conf
    # perl -pi -e "s/<sms>/master01/" /etc/ganglia/gmond.conf
    # # Add configuration to compute image and provide gridname
    # cp /etc/ganglia/gmond.conf $CHROOT/etc/ganglia/gmond.conf
    # echo "gridname MySite" | sudo tee -a /etc/ganglia/gmetad.conf
    # # Start and enable Ganglia services
    # systemctl enable --now gmond
    # systemctl enable --now gmetad
    # chroot $CHROOT systemctl enable gmond
    # # Restart web server
    # systemctl try-restart httpd
    # # Install ClusterShell
    # yum -y install clustershell-ohpc
    # # Setup node definitions
    # cd /etc/clustershell/groups.d &&  mv local.cfg local.cfg.orig
    # echo "adm: master01" | sudo tee  local.cfg
    # echo "compute: compute0[1-2]" | sudo tee -a local.cfg
    # echo "all: @adm,@compute" | sudo tee -a local.cfg
    # # The Warewulf system includes functionality to import arbitrary files from the provisioning server for distribution to managed hosts.
    # wwsh file list
    # wwsh file import /etc/passwd
    # wwsh file import /etc/group
    # wwsh file import /etc/shadow
    # wwsh file list
    # # (Optional) Include drivers from kernel updates; needed if enabling additional kernel modules on computes
    # export WW_CONF=/etc/warewulf/bootstrap.conf
    # echo "drivers += updates/kernel/" >> $WW_CONF
    # # (Optional) Include overlayfs drivers; needed by Singularity
    # # echo "drivers += overlay" >> $WW_CONF
    # export WW_CONF="drivers += overlay":$WW_CONF
    # # Build bootstrap image
    # wwbootstrap `uname -r`
    # # Assemble Virtual Node File System (VNFS) image
    # wwvnfs --chroot $CHROOT
    # # Set provisioning interface as the default networking device
    # echo "GATEWAYDEV=eth0" > /tmp/network.$$
    # wwsh -y file import /tmp/network.$$ --name network
    # wwsh -y file set network --path /etc/sysconfig/network --mode=0644 --uid=0
    # wwsh file list
    # # Add nodes to Warewulf data store
    # # eth0 public network on master01 eth1 private network on compute01 compute02
    # wwsh -y node new compute01 --ipaddr=192.168.1.253 --hwaddr=08:00:27:e3:b0:01 -D eth0
    # wwsh -y node new compute02 --ipaddr=192.168.1.252 --hwaddr=08:00:27:77:86:f5 -D eth0
    # wwsh file list
    # # Define provisioning image for hosts
    # wwsh -y provision set "compute01" --vnfs=centos7.6 --bootstrap=`uname -r` --files=dynamic_hosts,passwd,group,shadow,network
    # wwsh -y provision set "compute02" --vnfs=centos7.6 --bootstrap=`uname -r` --files=dynamic_hosts,passwd,group,shadow,network
    # wwsh provision list
    # sudo systemctl restart gmond
    # sudo systemctl restart gmetad
    # # Restart dhcp / update PXE
    # sudo systemctl restart dhcpd
    # sudo wwsh pxe update
    # # start pbspro daemons on master host
    # systemctl enable pbs
    # systemctl start pbs
    # # initialize PBS path
    # # sudo NOT WORKING HAS TO BE ROOT
    # source /etc/profile.d/pbs.sh
    # # enable user environment propagation (needed for modules support)
    # qmgr -c "set server default_qsub_arguments= -V"
    # # enable uniform multi-node MPI task distribution
    # qmgr -c "set server resources_default.place=scatter"
    # # enable support for job accounting
    # qmgr -c "set server job_history_enable=True"
    # # register compute hosts with pbspro
    # qmgr -c "create node compute01"
    # qmgr -c "create node compute02"
    # # sudo NOT WORKING HAS TO BE ROOT
    # pbsnodes -a
    # # Run a Test Job
    # useradd -m test
    # wwsh file resync passwd shadow group
    # wwsh file list
    # hostnamectl status
    SHELL
  end


  config.vm.define "compute01" do |hpcluster|
    hpcluster.vm.box = "bento/centos-7.6"
    hpcluster.vm.hostname = "compute01"
    hpcluster.vm.network "private_network", ip: "192.168.1.253"
    hpcluster.vm.provider "virtualbox" do |vb|
        vb.name = "compute01"
        vb.memory = "512"
    end
    hpcluster.vm.provision "ansible_local" do |ansible|
    ansible.playbook = "deploy.yml"
    ansible.become = true
    ansible.compatibility_mode = "2.0"
    ansible.version = "2.8.2"
    end
    hpcluster.vm.provision "shell", inline: <<-SHELL
    hostnamectl status
    SHELL
  end

  config.vm.define "compute02" do |hpcluster|
    hpcluster.vm.box = "bento/centos-7.6"
    hpcluster.vm.hostname = "compute02"
    hpcluster.vm.network "private_network", ip: "192.168.1.252"
    hpcluster.vm.provider "virtualbox" do |vb|
        vb.name = "compute02"
        vb.memory = "512"
    end
    hpcluster.vm.provision "ansible_local" do |ansible|
    ansible.playbook = "deploy.yml"
    ansible.become = true
    ansible.compatibility_mode = "2.0"
    ansible.version = "2.8.2"
    end
    hpcluster.vm.provision "shell", inline: <<-SHELL
    hostnamectl status
    SHELL
  end

end
