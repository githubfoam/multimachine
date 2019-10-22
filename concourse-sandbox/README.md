# concourse sandbox

~~~
vagrant up  
vagrant ssh  

wget https://raw.githubusercontent.com/starkandwayne/concourse-tutorial/master/docker-compose.yml

docker-compose up -d

[vagrant@control01 ~]$ docker image ls
REPOSITORY            TAG                 IMAGE ID            CREATED             SIZE
postgres              latest              f88dfa384cc4        5 days ago          348MB
concourse/concourse   5.6.0               fd37c1713462        2 weeks ago         1.29GB

[vagrant@control01 ~]$ docker container ls
CONTAINER ID        IMAGE                       COMMAND                  CREATED             STATUS              PORTS                    NAMES
93fe6bd5a85d        concourse/concourse:5.6.0   "dumb-init /usr/loca…"   4 hours ago         Up 4 hours          0.0.0.0:8080->8080/tcp   vagrant_concourse_1
ab7577c8235e        postgres                    "docker-entrypoint.s…"   4 hours ago         Up 4 hours          5432/tcp                 vagrant_concourse-db_1

[vagrant@control01 ~]$ docker inspect concourse/concourse:5.6.0

http://192.168.45.41:8080/

https://github.com/concourse/concourse#quick-start
~~~
