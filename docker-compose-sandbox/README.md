# dockerization sandbox

~~~
vagrant up  
vagrant ssh  
[vagrant@control01 ~]$ sudo docker-compose -f /vagrant/hello_world/docker-compose.yml build
[vagrant@control01 ~]$ sudo docker image ls
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
hello_world_web     latest              852adcc08c8a        2 minutes ago       892MB
python              2.7                 d0ca2da1bc25        25 hours ago        887MB
[vagrant@control01 ~]$ sudo docker container ls
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
[vagrant@control01 ~]$ sudo docker ps -a
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
[vagrant@control01 ~]$
~~~
~~~
[vagrant@control01 ~]$ sudo docker-compose -f /vagrant/hello_world/docker-compose.yml up -d
[vagrant@control01 ~]$ sudo docker ps -a
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                NAMES
60c2c887b189        hello_world_web     "python app.py"          5 minutes ago       Up 5 minutes        0.0.0.0:80->80/tcp   hello_world_web_1
22f8218c0bf1        redis               "docker-entrypoint.s…"   5 minutes ago       Up 5 minutes        6379/tcp             hello_world_redis_1
[vagrant@control01 ~]$ sudo docker container ls
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                NAMES
60c2c887b189        hello_world_web     "python app.py"          5 minutes ago       Up 5 minutes        0.0.0.0:80->80/tcp   hello_world_web_1
22f8218c0bf1        redis               "docker-entrypoint.s…"   5 minutes ago       Up 5 minutes        6379/tcp             hello_world_redis_1


[vagrant@control01 ~]$ docker inspect --format='{{.Name}} - {{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(docker ps -aq) | sed 's/ \// /'
/hello_world_web_1 - 172.17.0.3
/hello_world_redis_1 - 172.17.0.2
[vagrant@control01 ~]$ docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' hello_world_web_1
172.17.0.3
[vagrant@control01 ~]$ WEB_APP_IP=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' hello_world_web_1)
[vagrant@control01 ~]$ echo $WEB_APP_IP
172.17.0.3
[vagrant@control01 ~]$ curl http://${WEB_APP_IP}:80
<h3>Hello World!</h3><b>Visits:</b> 1<br/>

browse http://http://192.168.45.41/
~~~
integration tests(CI)
~~~
-p to indicate a specific project name

[vagrant@control01 ~]$ sudo docker-compose -f /vagrant/hello_world/docker-compose.test.yml -p ci build
[vagrant@control01 ~]$ sudo docker ps -a
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                NAMES
60c2c887b189        hello_world_web     "python app.py"          41 minutes ago      Up 40 minutes       0.0.0.0:80->80/tcp   hello_world_web_1
22f8218c0bf1        redis               "docker-entrypoint.s…"   41 minutes ago      Up 41 minutes       6379/tcp             hello_world_redis_1
[vagrant@control01 ~]$ sudo docker image ls
REPOSITORY          TAG                 IMAGE ID            CREATED              SIZE
ci_sut              latest              102f2ee44973        About a minute ago   162MB
ci_web              latest              852adcc08c8a        45 minutes ago       892MB
hello_world_web     latest              852adcc08c8a        45 minutes ago       892MB
python              2.7                 d0ca2da1bc25        26 hours ago         887MB
redis               latest              f7302e4ab3a8        4 weeks ago          98.2MB
ubuntu              xenial              5e13f8dd4c1a        7 weeks ago          120MB


[vagrant@control01 ~]$ sudo docker-compose -f /vagrant/hello_world/docker-compose.test.yml -p ci up -d
Creating ci_redis_1 ... done                                                                                                                                                                                       Creating ci_web_1   ... done                                                                                                                                                                                       Creating ci_sut_1   ... done                                                                                                                                                                                       [vagrant@control01 ~]$ sudo docker ps -a
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                      PORTS                NAMES
47e1327aba41        ci_sut              "bash test.sh"           14 seconds ago      Exited (2) 10 seconds ago                        ci_sut_1
43b15bade2a4        ci_web              "python app.py"          17 seconds ago      Up 14 seconds               80/tcp               ci_web_1
4e9e3fe618bc        redis               "docker-entrypoint.s…"   23 seconds ago      Up 16 seconds               6379/tcp             ci_redis_1
60c2c887b189        hello_world_web     "python app.py"          42 minutes ago      Up 42 minutes               0.0.0.0:80->80/tcp   hello_world_web_1
22f8218c0bf1        redis               "docker-entrypoint.s…"   42 minutes ago      Up 42 minutes               6379/tcp             hello_world_redis_1
~~~
~~~
[vagrant@control01 ~]$ cd /vagrant/hello_world/
[vagrant@control01 hello_world]$ docker-compose ps
       Name                      Command               State         Ports
---------------------------------------------------------------------------------
hello_world_redis_1   docker-entrypoint.sh redis ...   Up      6379/tcp
hello_world_web_1     python app.py                    Up      0.0.0.0:80->80/tcp

[vagrant@control01 hello_world]$ docker-compose down
Stopping hello_world_web_1   ... done                                                                                                                                                                              Stopping hello_world_redis_1 ... done                                                                                                                                                                              Removing hello_world_web_1   ... done                                                                                                                                                                              Removing hello_world_redis_1 ... done                                                                                                                                                                              [vagrant@control01 hello_world]$ docker-compose ps
Name   Command   State   Ports
------------------------------

[vagrant@control01 hello_world]$ sudo docker ps -a
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                      PORTS               NAMES
47e1327aba41        ci_sut              "bash test.sh"           11 minutes ago      Exited (2) 11 minutes ago                       ci_sut_1
43b15bade2a4        ci_web              "python app.py"          12 minutes ago      Up 11 minutes               80/tcp              ci_web_1
4e9e3fe618bc        redis               "docker-entrypoint.s…"   12 minutes ago      Up 12 minutes               6379/tcp            ci_redis_1

[vagrant@control01 hello_world]$ docker-compose -p ci stop
Stopping ci_web_1   ... done                                                                                                                                                                                       Stopping ci_redis_1 ... done    
[vagrant@control01 hello_world]$ sudo docker ps -a
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                        PORTS               NAMES
47e1327aba41        ci_sut              "bash test.sh"           15 minutes ago      Exited (2) 15 minutes ago                         ci_sut_1
43b15bade2a4        ci_web              "python app.py"          15 minutes ago      Exited (137) 20 seconds ago                       ci_web_1
4e9e3fe618bc        redis               "docker-entrypoint.s…"   15 minutes ago      Exited (0) 20 seconds ago                         ci_redis_1
~~~

~~~
[vagrant@control01 hello_world]$ sudo docker-compose -p ci stop
Stopping ci_web_1   ... done                                                                                                                                                                                       Stopping ci_redis_1 ... done                                                                                                                                                                                       [vagrant@control01 hello_world]$ sudo docker-compose -p ci ps
   Name                 Command                State     Ports
--------------------------------------------------------------
ci_redis_1   docker-entrypoint.sh redis ...   Exit 0
ci_web_1     python app.py                    Exit 137


[vagrant@control01 hello_world]$ docker-compose -p ci stop
Stopping ci_web_1   ... done                                                                                                                                                                                       Stopping ci_redis_1 ... done                                                                                                                                                                                       [vagrant@control01 hello_world]$ docker-compose stop
Stopping hello_world_web_1   ... done                                                                                                                                                                              Stopping hello_world_redis_1 ... done                  
[vagrant@control01 hello_world]$ docker-compose ps
       Name                      Command                State     Ports
-----------------------------------------------------------------------
hello_world_redis_1   docker-entrypoint.sh redis ...   Exit 0
hello_world_web_1     python app.py                    Exit 137
~~~
