~~~
vagrant@manager01:~$ sudo curl -L "https://github.com/docker/compose/releases/download/1.24.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   617    0   617    0     0    882      0 --:--:-- --:--:-- --:--:--   882
100 15.4M  100 15.4M    0     0  2387k      0  0:00:06  0:00:06 --:--:-- 3593k
vagrant@manager01:~$ sudo chmod +x /usr/local/bin/docker-compose && sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
vagrant@manager01:~$ sudo docker-compose --version
docker-compose version 1.24.1, build 4667896b
~~~
~~~

vagrant@manager01:~$ sudo docker node ls
ID                            HOSTNAME            STATUS              AVAILABILITY        MANAGER STATUS
64h26d3h926rsbzuti2rlcych     worker2             Ready               Active
algs4at5mno6tiak2v4qxr17b     worker1             Ready               Active
ex91es3aijisnt4q6lyauvi8h     manager             Ready               Active              Unreachable
m3wt1j3kzwxef23z7lyzak247 *   manager01           Ready               Active              Leader           Ready               Active              Leader

vagrant@manager01:~$ sudo docker service create --name registry --publish published=5000,target=5000 registry:2
n2nbknwyqc5hoqtj9z94p4zc8
Since --detach=false was not specified, tasks will be created in the background.
In a future release, --detach=false will become the default.
vagrant@manager01:~$ docker service ls
ID                  NAME                MODE                REPLICAS            IMAGE               PORTS
n2nbknwyqc5h        registry            replicated          1/1                 registry:2          *:5000->5000/tcp
vagrant@manager01:~$

vagrant@manager01:~$ docker service ps registry
ID                  NAME                IMAGE               NODE                DESIRED STATE       CURRENT STATE           ERROR               PORTS
psywso47fetp        registry.1          registry:2          worker2             Running             Running 2 minutes ago
vagrant@manager01:~$ sudo docker service scale registry=2
registry scaled to 2
vagrant@manager01:~$ docker service ps registry
ID                  NAME                IMAGE               NODE                DESIRED STATE       CURRENT STATE            ERROR               PORTS
psywso47fetp        registry.1          registry:2          worker2             Running             Running 3 minutes ago
4khzo05wwve7        registry.2          registry:2          manager01           Running             Running 18 seconds ago

vagrant@manager01:~$ curl http://localhost:5000/v2/
{}vagrant@manager01:~$

  vagrant@manager01:~$ docker-compose -f /vagrant/hello_world/docker-compose.yml up -d
  WARNING: The Docker Engine you're using is running in swarm mode.

  Compose does not use swarm mode to deploy services to multiple nodes in a swarm. All containers will be scheduled on the current node.

  To deploy your application across the swarm, use `docker stack deploy`.

  Creating network "hello_world_default" with the default driver
  Creating hello_world_redis_1 ... done                                                                                                                                                                              Creating hello_world_web_1   ... done
  vagrant@manager01:~$ docker-compose -f /vagrant/hello_world/docker-compose.yml ps
         Name                      Command               State         Ports
  ---------------------------------------------------------------------------------
  hello_world_redis_1   docker-entrypoint.sh redis ...   Up      6379/tcp
  hello_world_web_1     python app.py                    Up      0.0.0.0:80->80/tcp

  vagrant@manager01:~$ docker inspect --format='{{.Name}} - {{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(docker ps -aq) | sed 's/ \// /'
  /hello_world_web_1 - 172.19.0.3
  /hello_world_redis_1 - 172.19.0.2
  /registry.2.4khzo05wwve73nz38t310rrbk - 10.255.0.8
  vagrant@manager01:~$  WEB_APP_IP=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' hello_world_web_1)
  vagrant@manager01:~$ echo $WEB_APP_IP
  172.19.0.3
  vagrant@manager01:~$ curl http://${WEB_APP_IP}:80
  <h3>Hello World!</h3><b>Visits:</b> 1<br/>
  vagrant@manager01:~$

  Bring the app down
  vagrant@manager01:~$ docker-compose -f /vagrant/hello_world/docker-compose.yml down
  Stopping hello_world_web_1   ... done                                                                                                                                                                              Stopping hello_world_redis_1 ... done                                                                                                                                                                              Removing hello_world_web_1   ... done                                                                                                                                                                              Removing hello_world_redis_1 ... done                                                                                                                                                                              Removing network hello_world_default

Push the generated image to the registry
vagrant@manager01:~$ docker-compose -f /vagrant/hello_world/docker-compose.yml push

Deploy the stack to the swarm
vagrant@manager01:~$ docker stack deploy  --compose-file /vagrant/hello_world/docker-compose.yml hello_world
Ignoring unsupported options: build, links

Creating service hello_world_web
Updating service hello_world_redis (id: q3hii5w5g5m5mjfp9hz311uls)

vagrant@manager01:~$ docker stack services hello_world
ID                  NAME                MODE                REPLICAS            IMAGE                        PORTS
q3hii5w5g5m5        hello_world_redis   replicated          1/1                 redis:latest
sfbby2e26807        hello_world_web     replicated          0/1                 127.0.0.1:5000/hello_world   *:80->80/tcp

vagrant@manager01:~$ docker stack ls
NAME         SERVICES
hello_world  2

vagrant@manager01:~$ docker stack ps hello_world
ID                  NAME                    IMAGE                        NODE                DESIRED STATE       CURRENT STATE                     ERROR                              PORTS
3is06a2dfqn7        hello_world_web.1       127.0.0.1:5000/hello_world   manager             Ready               Rejected less than a second ago   "No such image: 127.0.0.1:5000…"
y1cwn19i8r7t         \_ hello_world_web.1   127.0.0.1:5000/hello_world   manager             Shutdown            Rejected less than a second ago   "No such image: 127.0.0.1:5000…"
s6mdzzud6r0w         \_ hello_world_web.1   127.0.0.1:5000/hello_world   manager             Shutdown            Rejected less than a second ago   "No such image: 127.0.0.1:5000…"
m9xhdytbiq0n         \_ hello_world_web.1   127.0.0.1:5000/hello_world   manager             Shutdown            Rejected less than a second ago   "No such image: 127.0.0.1:5000…"
5ygizy0p0ius         \_ hello_world_web.1   127.0.0.1:5000/hello_world   manager             Shutdown            Rejected less than a second ago   "No such image: 127.0.0.1:5000…"
ze2nzegfohjq        hello_world_redis.1     redis:latest                 worker1             Running             Running 4 minutes ago

vagrant@manager01:~$ docker stack rm hello_world
Removing service hello_world_redis
Removing service hello_world_web
Removing network hello_world_default
vagrant@manager01:~$ docker service rm registry
registry
~~~
