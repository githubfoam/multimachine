# dockerization sandbox

~~~
[vagrant@control01 ~]$ sudo docker container ls
CONTAINER ID        IMAGE                       COMMAND                  CREATED              STATUS              PORTS                  NAMES
f18dcf6c1d7f        corbinu/docker-phpmyadmin   "/bin/sh -c phpmyadm…"   About a minute ago   Up 56 seconds       0.0.0.0:8181->80/tcp   wordpress_phpmyadmin_1
2fcab611d1fe        wordpress                   "docker-entrypoint.s…"   9 minutes ago        Up 9 minutes        0.0.0.0:8080->80/tcp   wordpress_wordpress_1
97a36edcc5ed        mariadb                     "docker-entrypoint.s…"   9 minutes ago        Up 9 minutes        3306/tcp               wordpress_wordpress_db_1

[vagrant@control01 ~]$ sudo docker-compose -f /vagrant/wordpress/docker-compose.yml ps
          Name                        Command               State          Ports
----------------------------------------------------------------------------------------
wordpress_phpmyadmin_1     /bin/sh -c phpmyadmin-start      Up      0.0.0.0:8181->80/tcp
wordpress_wordpress_1      docker-entrypoint.sh apach ...   Up      0.0.0.0:8080->80/tcp
wordpress_wordpress_db_1   docker-entrypoint.sh mysqld      Up      3306/tcp

[vagrant@control01 ~]$ sudo docker-compose -f /vagrant/wordpress/docker-compose.yml images
       Container                  Repository            Tag       Image Id      Size
-------------------------------------------------------------------------------------
wordpress_phpmyadmin_1     corbinu/docker-phpmyadmin   latest   5c663962b799   451 MB
wordpress_wordpress_1      wordpress                   latest   92682699fd7d   478 MB
wordpress_wordpress_db_1   mariadb                     latest   99c1098d5884   339 MB
[vagrant@control01 ~]$ sudo docker-compose -f /vagrant/wordpress/docker-compose.yml stop
Stopping wordpress_phpmyadmin_1   ... done                                                                                                                                                                         Stopping wordpress_wordpress_1    ... done                                                                                                                                                                         Stopping wordpress_wordpress_db_1 ... done                                                                                                                                                                         [vagrant@control01 ~]$ sudo docker-compose -f /vagrant/wordpress/docker-compose.yml rm
Going to remove wordpress_phpmyadmin_1, wordpress_wordpress_1, wordpress_wordpress_db_1
Are you sure? [yN] y
Removing wordpress_phpmyadmin_1   ... done                                                                                                                                                                         Removing wordpress_wordpress_1    ... done                                                                                                                                                                         Removing wordpress_wordpress_db_1 ... done                                                                                                                                                                         [vagrant@control01 ~]$ sudo docker-compose -f /vagrant/wordpress/docker-compose.yml up -d
Creating wordpress_wordpress_db_1 ... done                                                                                                                                                                         Creating wordpress_phpmyadmin_1   ... done                                                                                                                                                                         Creating wordpress_wordpress_1    ... done  


browse
http://192.168.45.41:8181
~~~
~~~
References:
https://www.digitalocean.com/community/tutorials/how-to-install-wordpress-and-phpmyadmin-with-docker-compose-on-ubuntu-14-04

https://github.com/phpmyadmin/docker
~~~
