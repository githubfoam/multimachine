# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.

# https://computingforgeeks.com/setup-etcd-cluster-on-centos-debian-ubuntu/
$etcd1_script = <<SCRIPT
# Install etcd
mkdir -p /tmp/etcd && cd /tmp/etcd && sudo apt-get -y install wget && \
curl -s https://api.github.com/repos/etcd-io/etcd/releases/latest \
  | grep browser_download_url \
  | grep linux-amd64 \
  | cut -d '"' -f 4 \
  | wget -qi -
  tar xvf *.tar.gz
  cd etcd-*/
  sudo mv etcd* /usr/local/bin/
  cd ~
rm -rf /tmp/etcd
etcd --version
etcdctl --version
sudo groupadd --system etcd
sudo useradd -s /sbin/nologin --system -g etcd etcd
sudo mkdir -p /var/lib/etcd/
sudo mkdir /etc/etcd
sudo chown -R etcd:etcd /var/lib/etcd/
cat <<EOF | sudo tee /etc/systemd/system/etcd.service
[Unit]
Description=etcd service
Documentation=https://github.com/etcd-io/etcd

[Service]
Type=notify
User=etcd
ExecStart=/usr/local/bin/etcd \\
  --name etcd1 \\
  --data-dir=/var/lib/etcd \\
  --initial-advertise-peer-urls http://192.168.18.9:2380 \\
  --listen-peer-urls http://192.168.18.9:2380 \\
  --listen-client-urls http://192.168.18.9:2379,http://127.0.0.1:2379 \\
  --advertise-client-urls http://192.168.18.9:2379 \\
  --initial-cluster-token etcd-cluster-0 \\
  --initial-cluster etcd1=http://etcd1:2380,etcd2=http://etcd2:2380,etcd3=http://etcd3:2380 \\
  --initial-cluster-state new \

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable etcd
# sudo systemctl start etcd
# sudo systemctl status etcd -l
SCRIPT
$etcd2_script = <<SCRIPT
# Install etcd
mkdir -p /tmp/etcd && cd /tmp/etcd && sudo apt-get -y install wget && \
curl -s https://api.github.com/repos/etcd-io/etcd/releases/latest \
  | grep browser_download_url \
  | grep linux-amd64 \
  | cut -d '"' -f 4 \
  | wget -qi -
  tar xvf *.tar.gz
  cd etcd-*/
  sudo mv etcd* /usr/local/bin/
  cd ~
rm -rf /tmp/etcd
etcd --version
etcdctl --version
sudo groupadd --system etcd
sudo useradd -s /sbin/nologin --system -g etcd etcd
sudo mkdir -p /var/lib/etcd/
sudo mkdir /etc/etcd
sudo chown -R etcd:etcd /var/lib/etcd/
cat <<EOF | sudo tee /etc/systemd/system/etcd.service
[Unit]
Description=etcd service
Documentation=https://github.com/etcd-io/etcd

[Service]
Type=notify
User=etcd
ExecStart=/usr/local/bin/etcd \\
  --name etcd2 \\
  --data-dir=/var/lib/etcd \\
  --initial-advertise-peer-urls http://192.168.18.10:2380 \\
  --listen-peer-urls http://192.168.18.10:2380 \\
  --listen-client-urls http://192.168.18.10:2379,http://127.0.0.1:2379 \\
  --advertise-client-urls http://192.168.18.10:2379 \\
  --initial-cluster-token etcd-cluster-0 \\
  --initial-cluster etcd1=http://etcd1:2380,etcd2=http://etcd2:2380,etcd3=http://etcd3:2380 \\
  --initial-cluster-state new \

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable etcd
# sudo systemctl start etcd
# sudo systemctl status etcd -l
SCRIPT
$etcd3_script = <<SCRIPT
# Install etcd
mkdir -p /tmp/etcd && cd /tmp/etcd && sudo apt-get -y install wget && \
curl -s https://api.github.com/repos/etcd-io/etcd/releases/latest \
  | grep browser_download_url \
  | grep linux-amd64 \
  | cut -d '"' -f 4 \
  | wget -qi -
  tar xvf *.tar.gz
  cd etcd-*/
  sudo mv etcd* /usr/local/bin/
  cd ~
rm -rf /tmp/etcd
etcd --version
etcdctl --version
sudo groupadd --system etcd
sudo useradd -s /sbin/nologin --system -g etcd etcd
sudo mkdir -p /var/lib/etcd/
sudo mkdir /etc/etcd
sudo chown -R etcd:etcd /var/lib/etcd/
cat <<EOF | sudo tee /etc/systemd/system/etcd.service
[Unit]
Description=etcd service
Documentation=https://github.com/etcd-io/etcd

[Service]
Type=notify
User=etcd
ExecStart=/usr/local/bin/etcd \\
  --name etcd3 \\
  --data-dir=/var/lib/etcd \\
  --initial-advertise-peer-urls http://192.168.18.11:2380 \\
  --listen-peer-urls http://192.168.18.11:2380 \\
  --listen-client-urls http://192.168.18.11:2379,http://127.0.0.1:2379 \\
  --advertise-client-urls http://192.168.18.11:2379 \\
  --initial-cluster-token etcd-cluster-0 \\
  --initial-cluster etcd1=http://etcd1:2380,etcd2=http://etcd2:2380,etcd3=http://etcd3:2380 \\
  --initial-cluster-state new \

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable etcd
# sudo systemctl start etcd
# sudo systemctl status etcd -l
SCRIPT
Vagrant.configure("2") do |config|
  config.vm.provider "virtualbox" do |vb|
    vb.gui = false
    vb.memory = "512"
    vb.cpus = 1
  end

  config.vm.define "etcd1" do |webtier|
    webtier.vm.box = "bento/ubuntu-19.04"
    webtier.vm.hostname = "etcd1"
    webtier.vm.network "private_network", ip: "192.168.18.9"
    webtier.vm.provider "virtualbox" do |vb|
        vb.name = "etcd1"
    end
    webtier.vm.provision "ansible_local" do |ansible|
    ansible.playbook = "deploy.yml"
    ansible.become = true
    ansible.compatibility_mode = "2.0"
    ansible.version = "2.8.4"
    ansible.galaxy_roles_path = "/etc/ansible/roles"
      end
    webtier.vm.provision "shell", inline: <<-SHELL
    hostnamectl status
    SHELL
    webtier.vm.provision "shell", inline: $etcd1_script, privileged: false
    end


    config.vm.define "etcd2" do |webtier|
      webtier.vm.box = "bento/ubuntu-19.04"
      webtier.vm.hostname = "etcd2"
      webtier.vm.network "private_network", ip: "192.168.18.10"
      webtier.vm.provider "virtualbox" do |vb|
          vb.name = "etcd2"
      end
      webtier.vm.provision "ansible_local" do |ansible|
      ansible.playbook = "deploy.yml"
      ansible.become = true
      ansible.compatibility_mode = "2.0"
      ansible.version = "2.8.4"
      ansible.galaxy_roles_path = "/etc/ansible/roles"
        end
      webtier.vm.provision "shell", inline: <<-SHELL
      hostnamectl status
      SHELL
      webtier.vm.provision "shell", inline: $etcd2_script, privileged: false
      end


      config.vm.define "etcd3" do |webtier|
        webtier.vm.box = "bento/ubuntu-19.04"
        webtier.vm.hostname = "etcd3"
        webtier.vm.network "private_network", ip: "192.168.18.11"
        webtier.vm.provider "virtualbox" do |vb|
            vb.name = "etcd3"
        end
        webtier.vm.provision "ansible_local" do |ansible|
        ansible.playbook = "deploy.yml"
        ansible.become = true
        ansible.compatibility_mode = "2.0"
        ansible.version = "2.8.4"
        ansible.galaxy_roles_path = "/etc/ansible/roles"
          end
        webtier.vm.provision "shell", inline: <<-SHELL
        hostnamectl status
        SHELL
        webtier.vm.provision "shell", inline: $etcd3_script, privileged: false
        end

end
