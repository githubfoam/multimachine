# awx
At leasts 4GB of memory
At least 2 cpu cores
At least 20GB of space
https://github.com/ansible/awx/blob/devel/INSTALL.md#prerequisites

ansible 2.8.1  
CentOS Linux release 7.6.1810 (Core)  
http://192.168.45.28 (admin/password)

$ cd /tmp/awxcompose && sudo docker-compose ps  
$ cd /tmp/awxcompose && sudo docker-compose stop  
$ cd /tmp/awxcompose && sudo docker-compose start

$ ip a |grep inet |egrep -v "inet6|127.0.0.1"

$ sudo docker logs -f awx_task  
$ sudo docker ps

cat ~/awx/installer/inventory  
grep -v '^#' ~/awx/installer/inventory  
grep -Ev '^#|^$' ~/awx/installer/inventory  
cat /tmp/pgdocker/pgdata/pg_hba.conf  
