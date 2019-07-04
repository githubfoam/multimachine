#!/bin/bash
yum -y install docker make automake python2-pip git >/dev/null
echo "=======================starting docker==============================="
systemctl enable --now docker >/dev/null
pip install --upgrade pip >/dev/null
echo "=======================installing docker-compose====================="
pip install docker-compose >/dev/null
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.34.0/install.sh | bash >/dev/null
source ~/.bashrc >/dev/null
nvm install 8 &&  nvm use 8 >/dev/null
echo "=======================cloning awx==================================="
cd /opt &&   git clone https://github.com/ansible/awx && cd awx >/dev/null
echo "=======================configuring postgresql========================"
mkdir /opt/postgresql &&  sed -i 's:postgres_data_dir=/tmp/pgdocker:postgres_data_dir=/opt/postgresql:g' /opt/awx/installer/inventory >/dev/null
echo "=======================installing awx================================"
cd /opt/awx/installer &&  ansible-playbook -i inventory install.yml >/dev/null
echo "====================================================================="
echo "hello, $USER. $HOSTNAME up and running"
echo "====================================================================="
