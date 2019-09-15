switches
~~~
auto = ENV['AUTO_START_SWARM'] || true # create swarm auto mode
multi_manager =  true # create swarm multi manager mode
~~~
multi-master mode
~~~
>vagrant up
>vagrant ssh manager
vagrant@manager:~$ docker node ls
ID                            HOSTNAME            STATUS              AVAILABILITY        MANAGER STATUS      ENGINE VERSION
kscv757m5li5u3vkdy6ogj93h *   manager             Ready               Active              Leader              19.03.2
upkfbsb1cbbddfc7bbznqyze1     manager1            Ready               Active              Reachable           19.03.2
uxalnnzeegjzz6ep7549vyigc     worker1             Ready               Active                                  19.03.2
apxj1nh24lxxeqjul2nij5edh     worker2             Ready               Active                                  19.03.2

~~~
single manager mode
~~~
>vagrant up manager worker1 worker2
vagrant@manager:~$ docker node ls
ID                            HOSTNAME            STATUS              AVAILABILITY        MANAGER STATUS      ENGINE VERSION
5c2b9ro497usg825f56iogz6k *   manager             Ready               Active              Leader              19.03.2
ajpetxug7geccc3c9tof1yftk     worker1             Ready               Active                                  19.03.2
vg9krmqmszq6gcq1qgtebvej5     worker2             Ready               Active                                  19.03.2
~~~
manual mode
~~~
>vagrant ssh manager
vagrant@manager:~$ docker swarm init --advertise-addr 192.168.10.2
Swarm initialized: current node (w8zoe6aph3y0a5jpl3x9cuyu8) is now a manager.

To add a worker to this swarm, run the following command:

    docker swarm join \
    --token SWMTKN-1-0ox18tu2l1d3jxoc5enzdf1hugosx1hpnaraxkznp8mxxycrww-26uaow1zx9pwan9nps99tr3np \
    192.168.10.2:2377

To add a manager to this swarm, run 'docker swarm join-token manager' and follow the instructions.


vagrant@worker2:~$ docker swarm join \
>     --token SWMTKN-1-0ox18tu2l1d3jxoc5enzdf1hugosx1hpnaraxkznp8mxxycrww-26uaow1zx9pwan9nps99tr3np \
>     192.168.10.2:2377
This node joined a swarm as a worker.
vagrant@worker2:~$ docker node ls
Error response from daemon: This node is not a swarm manager. Worker nodes can't be used to view or modify cluster state. Please run this command on a manager node or promote the current node to a manager.
vagrant@worker2:~$

vagrant@worker1:~$ docker swarm join \
 >     --token SWMTKN-1-0ox18tu2l1d3jxoc5enzdf1hugosx1hpnaraxkznp8mxxycrww-26uaow1zx9pwan9nps99tr3np \
>     192.168.10.2:2377
This node joined a swarm as a worker.

vagrant@manager:~$ docker node ls
ID                            HOSTNAME            STATUS              AVAILABILITY        MANAGER STATUS
a0b0xdkfs6qfor9tmzqt0j2mt     worker1             Ready               Active
vnejn2bzuxp2cm9aw8vqrrgm5     worker2             Ready               Active
w8zoe6aph3y0a5jpl3x9cuyu8 *   manager             Ready               Active              Leader
~~~
smoke-tests
jenkins, SaaS - Software as a Service
~~~
sudo docker service create --name jenkins --replicas 1 --publish 8080:8080 jenkins:alpine

vagrant@manager:~$ sudo docker service ls
ID                  NAME                MODE                REPLICAS            IMAGE               PORTS
icxg72axqwdr        jenkins             replicated          1/1                 jenkins:alpine      *:8080->8080/tcp
vagrant@manager:~$ sudo docker service ps jenkins
ID                  NAME                IMAGE               NODE                DESIRED STATE       CURRENT STATE         ERROR               PORTS
vyu6uj1e041f        jenkins.1           jenkins:alpine      manager             Running             Running 2 hours ago

browse
http://192.168.10.2:8080

vagrant@manager:~$ sudo docker service scale jenkins=3
vagrant@manager:~$ sudo docker service ps jenkins
ID                  NAME                IMAGE               NODE                DESIRED STATE       CURRENT STATE              ERROR               PORTS
vyu6uj1e041f        jenkins.1           jenkins:alpine      manager             Running             Running 2 hours ago
vochf504nzzj        jenkins.2           jenkins:alpine      worker2             Running             Preparing 25 seconds ago
ii7dxzn0owdr        jenkins.3           jenkins:alpine      worker1             Running             Preparing 26 seconds ago

vagrant@manager:~$ sudo docker service ps jenkins
ID                  NAME                IMAGE               NODE                DESIRED STATE       CURRENT STATE            ERROR               PORTS
vyu6uj1e041f        jenkins.1           jenkins:alpine      manager             Running             Running 2 hours ago
vochf504nzzj        jenkins.2           jenkins:alpine      worker2             Running             Running 56 seconds ago
ii7dxzn0owdr        jenkins.3           jenkins:alpine      worker1             Running             Running 58 seconds ago
vagrant@manager:~$ sudo docker service ls
ID                  NAME                MODE                REPLICAS            IMAGE               PORTS
icxg72axqwdr        jenkins             replicated          3/3                 jenkins:alpine      *:8080->8080/tcp

browse
http://192.168.10.2:8080
http://192.168.10.3:8080
http://192.168.10.4:8080
~~~
jenkins, SaaS - Software as a Service
~~~
scale the service
vagrant@manager:~$ sudo docker service scale jenkins=3

updates have a delay of 6s
vagrant@manager:~$ sudo docker service update --update-delay 6s jenkins

rolling update of the service
vagrant@manager:~$ sudo docker service update --image  jenkins/jenkins:lts jenkins
vagrant@manager:~$ sudo docker service ps jenkins
ID                  NAME                IMAGE                 NODE                DESIRED STATE       CURRENT STATE                 ERROR               PORTS
10pqsj50iavt        jenkins.1           jenkins/jenkins:lts   manager             Running             Running 10 seconds ago
vyu6uj1e041f         \_ jenkins.1       jenkins:alpine        manager             Shutdown            Shutdown about a minute ago
99t6w5bqu84h        jenkins.2           jenkins/jenkins:lts   worker2             Running             Running about a minute ago
vochf504nzzj         \_ jenkins.2       jenkins:alpine        worker2             Shutdown            Shutdown 2 minutes ago
clq2st7pif14        jenkins.3           jenkins/jenkins:lts   worker1             Running             Running 2 minutes ago
ii7dxzn0owdr         \_ jenkins.3       jenkins:alpine        worker1             Shutdown            Shutdown 3 minutes ago

vagrant@manager:~$ docker service inspect --pretty jenkins

ID:             icxg72axqwdrx3rtn0nfhcwp8
Name:           jenkins
Service Mode:   Replicated
 Replicas:      3
UpdateStatus:
 State:         completed
 Started:       4 minutes
 Completed:     37 seconds
 Message:       update completed
Placement:
UpdateConfig:
 Parallelism:   1
 Delay:         6s
 On failure:    pause
 Monitoring Period: 5s
 Max failure ratio: 0
 Update order:      stop-first
RollbackConfig:
 Parallelism:   1
 On failure:    pause
 Monitoring Period: 5s
 Max failure ratio: 0
 Rollback order:    stop-first
ContainerSpec:
 Image:         jenkins/jenkins:lts@sha256:7cfe34701992434cc08bfd40e80e04ab406522214cf9bbefa57a5432a123b340
Resources:
Endpoint Mode:  vip
Ports:
 PublishedPort = 8080
  Protocol = tcp
  TargetPort = 8080
  PublishMode = ingress

  vagrant@manager:~$ sudo docker service rm jenkins
  jenkins  
~~~
nginx, SaaS - Software as a Service
~~~
vagrant@manager:~$ sudo docker service create -p 80:80 --name webserver nginx
g28vggkmxqd9aqr1ny463rbk9
Since --detach=false was not specified, tasks will be created in the background.
In a future release, --detach=false will become the default.
vagrant@manager:~$ sudo docker service ls
ID                  NAME                MODE                REPLICAS            IMAGE               PORTS
g28vggkmxqd9        webserver           replicated          1/1                 nginx:latest        *:80->80/tcp
vagrant@manager:~$ sudo docker service ps webserver
ID                  NAME                IMAGE               NODE                DESIRED STATE       CURRENT STATE            ERROR               PORTS
wh89n2o6bhmz        webserver.1         nginx:latest        worker2             Running             Running 16 seconds ago
vagrant@manager:~$ sudo docker service scale webserver=3
webserver scaled to 3
vagrant@manager:~$ sudo docker service ls
ID                  NAME                MODE                REPLICAS            IMAGE               PORTS
g28vggkmxqd9        webserver           replicated          1/3                 nginx:latest        *:80->80/tcp
vagrant@manager:~$ sudo docker service ps webserver
ID                  NAME                IMAGE               NODE                DESIRED STATE       CURRENT STATE              ERROR               PORTS
wh89n2o6bhmz        webserver.1         nginx:latest        worker2             Running             Running 3 minutes ago
n6djkefv06qv        webserver.2         nginx:latest        manager             Running             Preparing 12 seconds ago
nc3mpy6t9s3g        webserver.3         nginx:latest        manager01           Running             Preparing 12 seconds ago

vagrant@manager:~$ sudo docker service ps webserver
ID                  NAME                IMAGE               NODE                DESIRED STATE       CURRENT STATE            ERROR               PORTS
wh89n2o6bhmz        webserver.1         nginx:latest        worker2             Running             Running 3 minutes ago
n6djkefv06qv        webserver.2         nginx:latest        manager             Running             Running 27 seconds ago
nc3mpy6t9s3g        webserver.3         nginx:latest        manager01           Running             Running 28 seconds ago

browse
http://192.168.10.2:80

vagrant@manager:~$ sudo docker service rm webserver
webserver
~~~
nginx, SaaS - Software as a Service
~~~

vagrant@manager:~$docker service create -p 80:80 --name web nginx:latest
vagrant@manager:~$curl http://localhost:80
vagrant@manager:~$ docker service inspect web
vagrant@manager:~$ docker service scale web=5
vagrant@manager:~$ docker service ps web
ID                  NAME                IMAGE               NODE                DESIRED STATE       CURRENT STATE            ERROR               PORTS
oyd5237c2azv        web.1               nginx:latest        worker2             Running             Running 2 minutes ago
dn80i2nsawgs        web.2               nginx:latest        worker1             Running             Running 21 seconds ago
pi4owibtr90i        web.3               nginx:latest        manager             Running             Running 38 seconds ago
kc4k6blop06a        web.4               nginx:latest        manager01           Running             Running 38 seconds ago
qz24xs96dlh9        web.5               nginx:latest        manager01           Running             Running 38 seconds ago

# drain a particular node, that is remove all services from that node. The services will automatically be rescheduled on other nodes
vagrant@manager:~$ docker node update --availability drain manager
manager
vagrant@manager:~$ docker service ps web
ID                  NAME                IMAGE               NODE                DESIRED STATE       CURRENT STATE            ERROR               PORTS
oyd5237c2azv        web.1               nginx:latest        worker2             Running             Running 4 minutes ago
dn80i2nsawgs        web.2               nginx:latest        worker1             Running             Running 2 minutes ago
wmk9xhnj4p7s        web.3               nginx:latest        worker2             Running             Running 3 seconds ago
pi4owibtr90i         \_ web.3           nginx:latest        manager             Shutdown            Shutdown 4 seconds ago
kc4k6blop06a        web.4               nginx:latest        manager01           Running             Running 2 minutes ago
qz24xs96dlh9        web.5               nginx:latest        manager01           Running             Running 2 minutes ago
vagrant@manager:~$ docker node ls
ID                            HOSTNAME            STATUS              AVAILABILITY        MANAGER STATUS
64h26d3h926rsbzuti2rlcych     worker2             Ready               Active
algs4at5mno6tiak2v4qxr17b     worker1             Ready               Active
ex91es3aijisnt4q6lyauvi8h *   manager             Ready               Drain               Leader
m3wt1j3kzwxef23z7lyzak247     manager01           Ready               Active              Reachable

# scale down the service
vagrant@manager:~$ docker service scale web=4
web scaled to 4
vagrant@manager:~$ docker service ps web
ID                  NAME                IMAGE               NODE                DESIRED STATE       CURRENT STATE                 ERROR               PORTS
dn80i2nsawgs        web.2               nginx:latest        worker1             Running             Running 3 minutes ago
wmk9xhnj4p7s        web.3               nginx:latest        worker2             Running             Running about a minute ago
pi4owibtr90i         \_ web.3           nginx:latest        manager             Shutdown            Shutdown about a minute ago
kc4k6blop06a        web.4               nginx:latest        manager01           Running             Running 4 minutes ago
qz24xs96dlh9        web.5               nginx:latest        manager01           Running             Running 4 minutes ago

# bring node back online
vagrant@manager:~$ docker node ls
ID                            HOSTNAME            STATUS              AVAILABILITY        MANAGER STATUS
64h26d3h926rsbzuti2rlcych     worker2             Ready               Active
algs4at5mno6tiak2v4qxr17b     worker1             Ready               Active
ex91es3aijisnt4q6lyauvi8h *   manager             Ready               Drain               Leader
m3wt1j3kzwxef23z7lyzak247     manager01           Ready               Active              Reachable
vagrant@manager:~$ docker node update --availability active manager
manager
vagrant@manager:~$ docker node inspect manager --pretty
ID:                     ex91es3aijisnt4q6lyauvi8h
Hostname:               manager
Joined at:              2019-09-12 14:51:38.709206064 +0000 utc
Status:
 State:                 Ready
 Availability:          Active
 Address:               192.168.10.2
Manager Status:
 Address:               192.168.10.2:2377
 Raft Status:           Reachable
 Leader:                Yes
Platform:
 Operating System:      linux
 Architecture:          x86_64
Resources:
 CPUs:                  1
 Memory:                489.8MiB
Plugins:
 Network:               bridge, host, macvlan, null, overlay
 Volume:                local
Engine Version:         17.05.0-ce

vagrant@manager:~$ docker node ls
ID                            HOSTNAME            STATUS              AVAILABILITY        MANAGER STATUS
64h26d3h926rsbzuti2rlcych     worker2             Ready               Active
algs4at5mno6tiak2v4qxr17b     worker1             Ready               Active
ex91es3aijisnt4q6lyauvi8h *   manager             Ready               Active              Leader
m3wt1j3kzwxef23z7lyzak247     manager01           Ready               Active              Reachable

vagrant@manager:~$ docker service rm web
web
vagrant@manager:~$ docker service ls
ID                  NAME                MODE                REPLICAS            IMAGE               PORTS

https://github.com/docker/labs/blob/master/swarm-mode/beginner-tutorial/README.md#creating-the-nodes-and-swarm
~~~

add another manager
~~~
vagrant@manager:~$ sudo docker swarm init --advertise-addr 192.168.10.2
Swarm initialized: current node (ex91es3aijisnt4q6lyauvi8h) is now a manager.

To add a worker to this swarm, run the following command:

    docker swarm join \
    --token SWMTKN-1-3mniz9mlwh2kcx2wnqsjqawvebhf9e02d0lwnf8vkfq5arifzr-34ti53vretm17ud9qga08xeia \
    192.168.10.2:2377

To add a manager to this swarm, run 'docker swarm join-token manager' and follow the instructions.

vagrant@manager:~$ docker swarm join-token manager
To add a manager to this swarm, run the following command:

    docker swarm join \
    --token SWMTKN-1-3mniz9mlwh2kcx2wnqsjqawvebhf9e02d0lwnf8vkfq5arifzr-dnj1buyal1b2fbzxlcqn0dugs \
    192.168.10.2:2377

vagrant@manager:~$

vagrant@manager01:~$ sudo docker swarm join \
>     --token SWMTKN-1-3mniz9mlwh2kcx2wnqsjqawvebhf9e02d0lwnf8vkfq5arifzr-dnj1buyal1b2fbzxlcqn0dugs \
>     192.168.10.2:2377
This node joined a swarm as a manager.
vagrant@manager01:~$ sudo docker node ls
ID                            HOSTNAME            STATUS              AVAILABILITY        MANAGER STATUS
64h26d3h926rsbzuti2rlcych     worker2             Ready               Active
algs4at5mno6tiak2v4qxr17b     worker1             Ready               Active
ex91es3aijisnt4q6lyauvi8h     manager             Ready               Active              Leader
m3wt1j3kzwxef23z7lyzak247 *   manager01           Ready               Active              Reachable
~~~
example-voting-app
~~~
vagrant@manager01:~$ cd /vagrant
vagrant@manager01:/vagrant$ git clone https://github.com/docker/example-voting-app.git
vagrant@manager01:/vagrant$ cd example-voting-app/
vagrant@manager01:~$ docker stack deploy --compose-file /vagrant/example-voting-app/docker-stack.yml vote
Creating network vote_default
Creating network vote_frontend
Creating network vote_backend
Creating service vote_redis
Creating service vote_db
Creating service vote_vote
Creating service vote_result
Creating service vote_worker
Creating service vote_visualizer
vagrant@manager01:~$ docker stack services vote
ID                  NAME                MODE                REPLICAS            IMAGE                                          PORTS
3ch2f87mll41        vote_visualizer     replicated          0/1                 dockersamples/visualizer:stable                *:8080->8080/tcp
3sh9rlo40arj        vote_result         replicated          0/1                 dockersamples/examplevotingapp_result:before   *:5001->80/tcp
n6vc9qdatlgo        vote_redis          replicated          1/1                 redis:alpine
nmp2swecr0df        vote_worker         replicated          0/1                 dockersamples/examplevotingapp_worker:latest
pqyvghjieu5e        vote_db             replicated          0/1                 postgres:9.4
spkheq6t80e3        vote_vote           replicated          0/2                 dockersamples/examplevotingapp_vote:before     *:5000->80/tcp


vagrant@manager01:~$ docker stack ps vote
ID                  NAME                IMAGE                                          NODE                DESIRED STATE       CURRENT STATE                   ERROR                              PORTS
yae9t407u2za        vote_db.1           postgres:9.4                                   manager             Ready               Ready less than a second ago
ibl4e5kfyidx         \_ vote_db.1       postgres:9.4                                   manager01           Shutdown            Failed less than a second ago   "starting container failed: su…"
u4wu9v593lg8         \_ vote_db.1       postgres:9.4                                   manager             Shutdown            Failed 5 seconds ago            "starting container failed: su…"
aj1v0e73b1qo        vote_result.1       dockersamples/examplevotingapp_result:before   manager01           Running             Preparing 11 seconds ago
tbjvypu56g69        vote_db.1           postgres:9.4                                   manager             Shutdown            Failed 10 seconds ago           "starting container failed: su…"
fqvp3aqr3p35        vote_result.1       dockersamples/examplevotingapp_result:before   worker1             Shutdown            Failed 11 seconds ago           "starting container failed: su…"
utvbg5sjjo66        vote_db.1           postgres:9.4                                   manager01           Shutdown            Failed 16 seconds ago           "starting container failed: su…"
dh2s4q7j063x        vote_worker.1       dockersamples/examplevotingapp_worker:latest   manager             Running             Preparing 21 seconds ago
yj2asgx5rz9f        vote_result.1       dockersamples/examplevotingapp_result:before   worker1             Shutdown            Failed 16 seconds ago           "starting container failed: su…"
pjf3yq02s8sb        vote_db.1           postgres:9.4                                   manager01           Shutdown            Failed 22 seconds ago           "starting container failed: su…"
7o9pjv1tmrrr        vote_result.1       dockersamples/examplevotingapp_result:before   worker1             Shutdown            Failed 22 seconds ago           "starting container failed: su…"
o3rdyh0bgvzn         \_ vote_result.1   dockersamples/examplevotingapp_result:before   worker2             Shutdown            Failed 30 seconds ago           "starting container failed: su…"
blycj895fhik        vote_visualizer.1   dockersamples/visualizer:stable                manager             Running             Running about a minute ago
tk2hopqhu1dc        vote_worker.1       dockersamples/examplevotingapp_worker:latest   manager01           Shutdown            Failed 21 seconds ago           "starting container failed: su…"
zo20xfljzuar        vote_vote.1         dockersamples/examplevotingapp_vote:before     manager01           Running             Running 3 minutes ago
8dsagcoggej3        vote_redis.1        redis:alpine                                   worker1             Running             Running 3 minutes ago
e9ezyj5apufx        vote_vote.2         dockersamples/examplevotingapp_vote:before     worker2             Running             Running 3 minutes ago

vagrant@manager01:~$ docker stack ls
NAME  SERVICES
vote  6

vagrant@manager01:~$ curl http://localhost:5000

browse
http://192.168.10.12:5000/


Customize the app
docker-stack.yml.after

vagrant@manager01:~$ docker stack deploy --compose-file /vagrant/example-voting-app/docker-stack.yml vote
Updating service vote_redis (id: n6vc9qdatlgony0ltu37kgebv)
Updating service vote_db (id: pqyvghjieu5ed4wz5ltej13p9)
Updating service vote_vote (id: spkheq6t80e3saecnz0f5mnqu)
Updating service vote_result (id: 3sh9rlo40arjmw127x386noko)
Updating service vote_worker (id: nmp2swecr0dfy977t7uulcp46)
Updating service vote_visualizer (id: 3ch2f87mll4126e8j32vm0cc1)

vagrant@manager01:~$ docker stack rm vote
Removing service vote_visualizer
Removing service vote_result
Removing service vote_redis
Removing service vote_worker
Removing service vote_db
Removing service vote_vote
Removing network vote_default
Removing network vote_frontend
Removing network vote_backend

~~~
