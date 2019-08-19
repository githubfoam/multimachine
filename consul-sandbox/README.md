
# consul sandbox

~~~~
vagrant up
vagrant ssh vagrant-remotecontrol01
[vagrant@vagrant-remotecontrol01 ~]$ sudo ansible-playbook -i /vagrant/provisioning/hosts /vagrant/provisioning/00_initial.yml
[vagrant@vagrant-remotecontrol01 ~]$ sudo ansible-playbook -i /vagrant/provisioning/hosts /vagrant/provisioning/01_install.yml

vagrant@vagrant-remotecontrol01 ~]$ sudo ansible-inventory --inventory-file /vagrant/provisioning/hosts --graph
@all:
  |--@clients:
  |  |--vagrant-remotecontrol01
  |--@consulcluster:
  |  |--vagrant-consul-01
  |  |--vagrant-consul-02
  |  |--vagrant-consul-03
  |--@ungrouped:
[vagrant@vagrant-remotecontrol01 ~]$ sudo ansible --inventory-file /vagrant/provisioning/hosts vagrant-consul-03 -m shell -a "unzip version"
[vagrant@vagrant-remotecontrol01 ~]$ sudo ansible --inventory-file /vagrant/provisioning/hosts vagrant-consul-01 -m shell -a "yum list installed | grep unzip"
[vagrant@vagrant-remotecontrol01 ~]$ sudo ansible --inventory-file /vagrant/provisioning/hosts vagrant-consul-01 -m shell -a "consul version"
[vagrant@vagrant-remotecontrol01 ~]$ sudo ansible --inventory-file /vagrant/provisioning/hosts vagrant-consul-01 -m shell -a "ls -lai /usr/local/bin/consul"
$ sudo ansible --inventory-file /vagrant/provisioning/hosts vagrant-consul-01 -m shell -a "id consul"
$ sudo ansible --inventory-file /vagrant/provisioning/hosts vagrant-consul-01 -m shell -a "ls -ld /var/lib/consul"


[vagrant@vagrant-remotecontrol01 ~]$ sudo ansible --inventory-file /vagrant/provisioning/hosts vagrant-consul-01 -m shell -a "consul members"
vagrant-consul-01 | CHANGED | rc=0 >>
Node               Address             Status  Type    Build  Protocol  DC        Segment
vagrant-consul-01  192.168.18.9:8301   alive   server  1.5.3  2         tokyo-dc  <all>
vagrant-consul-02  192.168.18.10:8301  alive   server  1.5.3  2         tokyo-dc  <all>
vagrant-consul-03  192.168.18.11:8301  alive   server  1.5.3  2         tokyo-dc  <all>
URL
http://192.168.18.9:8500
http://192.168.18.10:8500
http://192.168.18.11:8500
~~~~
