# Zabbix 4.2 deployment

Set a password for the root user of the MariaDB server, leave other choices as default  
$ sudo mysql_secure_installation  

Create a database for Zabbix , skip password  
$ sudo mysql -uroot -p  
~~~~
MariaDB [(none)]> create database zabbix character set utf8 collate utf8_bin;  

Create a new database user called zabbix to access the new zabbix database:(set password as zabbix)  

MariaDB [(none)]> grant all privileges on zabbix.* to zabbix@localhost identified by 'zabbix';  
MariaDB [(none)]> flush privileges;  
MariaDB [(none)]> quit  
~~~~
 Import  the schema for the initial database into the newly created zabbix database ( password : zabbix)  
 $ sudo zcat /usr/share/doc/zabbix-server-mysql/create.sql.gz | mysql -uzabbix -p zabbix  

Set password for DB
$ sudo vi /etc/zabbix/zabbix_server.conf  
DBPassword=zabbix  
$ egrep -v "^#|^$" /etc/zabbix/zabbix_server.conf
~~~~
LogFile=/var/log/zabbix/zabbix_server.log
LogFileSize=0
PidFile=/var/run/zabbix/zabbix_server.pid
SocketDir=/var/run/zabbix
DBName=zabbix
DBUser=zabbix
DBPassword=zabbix
SNMPTrapperFile=/var/log/snmptrap/snmptrap.log
Timeout=4
AlertScriptsPath=/usr/lib/zabbix/alertscripts
ExternalScripts=/usr/lib/zabbix/externalscripts
FpingLocation=/usr/bin/fping
Fping6Location=/usr/bin/fping6
LogSlowQueries=3000
StatsAllowedIP=127.0.0.1
~~~~

Set timezone
$ sudo vi /etc/apache2/conf-enabled/zabbix.conf  
~~~~
<IfModule mod_php7.c>
    php_value max_execution_time 600
    php_value memory_limit 128M
    php_value post_max_size 32M
    php_value upload_max_filesize 16M
    php_value max_input_time 600
    php_value max_input_vars 10000
    php_value always_populate_raw_post_data -1
    php_value date.timezone Europe/Istanbul
</IfModule>
~~~~

$ sudo systemctl restart apache2.service && sudo systemctl enable --now zabbix-server.service  

http://192.168.45.25/zabbix

Web UI configuration
~~~~
Configure DB connection  
Password:zabbix  
Zabbix server details  
Nanme:zabbixsrv
Congratulations! You have successfully installed Zabbix frontend  
~~~~


~~~~
http://192.168.45.25/zabbix/index.php  
Admin/zabbix  
~~~~

Add hosts for monitoring Web UI
~~~~
Configuration - Hosts - Create Host
Host name : client-machine1
Groups : Linux servers
IP address : 192.168.45.26

Add new template to new host  
Templates - Template OS Linux - Add - Update

Configuration - Hosts - Enable - Zabbix Server
Configuration - Hosts - Enable - client-machine1

vagrant@client-machine1:~$ sudo systemctl restart zabbix-agent
~~~~


client-machine1  
~~~~
$ hostnamectl
Operating System: Ubuntu 18.10
$ ifconfig eth1
eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.45.26  netmask 255.255.255.0  broadcast 192.168.45.255
sudo apt install zabbix-agent  
sudo systemctl enable --now zabbix-agent
$ egrep -v "^#|^$" /etc/zabbix/zabbix_agentd.conf
PidFile=/var/run/zabbix/zabbix_agentd.pid
LogFile=/var/log/zabbix-agent/zabbix_agentd.log
LogFileSize=0
Server=192.168.45.25
ServerActive=127.0.0.1
Hostname=client-machine1
Include=/etc/zabbix/zabbix_agentd.conf.d/*.conf
~~~~

client-machine2  
~~~~
$ hostnamectl
Operating System: CentOS Linux 7 (Core)
$ ifconfig eth1
eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.45.27  netmask 255.255.255.0  broadcast 192.168.45.255
sudo rpm -Uvh https://repo.zabbix.com/zabbix/4.2/rhel/7/x86_64/zabbix-release-4.2-1.el7.noarch.rpm
sudo yum clean all
sudo yum -y install -y zabbix-agent
sudo systemctl enable --now zabbix-agent      
~~~~

zabbix-agent check
~~~~
sudo netstat -tulpn|grep zabbix  
telnet zabbix_agent_IP 10050
~~~~

~~~~
http://www.linuxpromagazine.com/Online/Features/Monitor-Your-Network-with-Zabbix/
https://www.zabbix.com/documentation/4.2/manual/concepts/agent
~~~~
