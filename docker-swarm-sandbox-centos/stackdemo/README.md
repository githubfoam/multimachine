~~~
vagrant@manager01:~$ docker service create --name registry --publish published=5000,target=5000 registry:2
j7czjwd6bgrpkd0f3mldibex4
Since --detach=false was not specified, tasks will be created in the background.
In a future release, --detach=false will become the default.
vagrant@manager01:~$ docker service ls
ID                  NAME                MODE                REPLICAS            IMAGE               PORTS
j7czjwd6bgrp        registry            replicated          1/1                 registry:2          *:5000->5000/tcp
vagrant@manager01:~$ curl http://localhost:5000/v2/
{}vagrant@manager01:~$ docker-compose -f /vagrant/stackdemo/docker-compose.yml up -d
WARNING: The Docker Engine you're using is running in swarm mode.

Compose does not use swarm mode to deploy services to multiple nodes in a swarm. All containers will be scheduled on the current node.

To deploy your application across the swarm, use `docker stack deploy`.

Creating network "stackdemo_default" with the default driver
Building web
Step 1/5 : FROM python:3
3: Pulling from library/python
4a56a430b2ba: Already exists                                                                                                                                                                                       4b5cacb629f5: Already exists                                                                                                                                                                                       14408c8d4f9a: Already exists                                                                                                                                                                                       ea67eaa7dd42: Already exists                                                                                                                                                                                       4d134ac3fe4b: Already exists                                                                                                                                                                                       4c55f6f5d7f0: Pull complete                                                                                                                                                                                        6ae475e50652: Pull complete                                                                                                                                                                                        6f4152644229: Pull complete                                                                                                                                                                                        6933d3d46042: Pull complete                                                                                                                                                                                        Digest: sha256:0f0e991a97426db345ca7ec59fa911c8ed27ced27c88ae9966b452bcc6438c2f
Status: Downloaded newer image for python:3
 ---> 02d2bb146b3b
Step 2/5 : ADD . /code
 ---> 1afb8fbb86c1
Removing intermediate container 7412099e89f1
Step 3/5 : WORKDIR /code
 ---> 0228310d49f3
Removing intermediate container 4f017446c75a
Step 4/5 : RUN pip install -r requirements.txt
 ---> Running in 89ece652136b
Collecting flask (from -r requirements.txt (line 1))
  Downloading https://files.pythonhosted.org/packages/9b/93/628509b8d5dc749656a9641f4caf13540e2cdec85276964ff8f43bbb1d3b/Flask-1.1.1-py2.py3-none-any.whl (94kB)
Collecting redis (from -r requirements.txt (line 2))
  Downloading https://files.pythonhosted.org/packages/bd/64/b1e90af9bf0c7f6ef55e46b81ab527b33b785824d65300bb65636534b530/redis-3.3.8-py2.py3-none-any.whl (66kB)
Collecting Jinja2>=2.10.1 (from flask->-r requirements.txt (line 1))
  Downloading https://files.pythonhosted.org/packages/1d/e7/fd8b501e7a6dfe492a433deb7b9d833d39ca74916fa8bc63dd1a4947a671/Jinja2-2.10.1-py2.py3-none-any.whl (124kB)
Collecting itsdangerous>=0.24 (from flask->-r requirements.txt (line 1))
  Downloading https://files.pythonhosted.org/packages/76/ae/44b03b253d6fade317f32c24d100b3b35c2239807046a4c953c7b89fa49e/itsdangerous-1.1.0-py2.py3-none-any.whl
Collecting Werkzeug>=0.15 (from flask->-r requirements.txt (line 1))
  Downloading https://files.pythonhosted.org/packages/b7/61/c0a1adf9ad80db012ed7191af98fa05faa95fa09eceb71bb6fa8b66e6a43/Werkzeug-0.15.6-py2.py3-none-any.whl (328kB)
Collecting click>=5.1 (from flask->-r requirements.txt (line 1))
  Downloading https://files.pythonhosted.org/packages/fa/37/45185cb5abbc30d7257104c434fe0b07e5a195a6847506c074527aa599ec/Click-7.0-py2.py3-none-any.whl (81kB)
Collecting MarkupSafe>=0.23 (from Jinja2>=2.10.1->flask->-r requirements.txt (line 1))
  Downloading https://files.pythonhosted.org/packages/98/7b/ff284bd8c80654e471b769062a9b43cc5d03e7a615048d96f4619df8d420/MarkupSafe-1.1.1-cp37-cp37m-manylinux1_x86_64.whl
Installing collected packages: MarkupSafe, Jinja2, itsdangerous, Werkzeug, click, flask, redis
Successfully installed Jinja2-2.10.1 MarkupSafe-1.1.1 Werkzeug-0.15.6 click-7.0 flask-1.1.1 itsdangerous-1.1.0 redis-3.3.8
 ---> 016399a003c7
Removing intermediate container 89ece652136b
Step 5/5 : CMD python app.py
 ---> Running in be067f2f8dbe
 ---> 8cc2663d3fae
Removing intermediate container be067f2f8dbe
Successfully built 8cc2663d3fae
Successfully tagged 127.0.0.1:5000/stackdemo:latest
WARNING: Image for service web was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling redis (redis:alpine)...
alpine: Pulling from library/redis
Digest: sha256:50899ea1ceed33fa03232f3ac57578a424faa1742c1ac9c7a7bdb95cdf19b858
Status: Downloaded newer image for redis:alpine
Creating stackdemo_web_1   ... done                                                                                                                                                                                Creating stackdemo_redis_1 ... done                                                                                                                                                                                vagrant@manager01:~$
vagrant@manager01:~$ docker-compose -f /vagrant/stackdemo/docker-compose.yml ps
      Name                     Command               State           Ports
-----------------------------------------------------------------------------------
stackdemo_redis_1   docker-entrypoint.sh redis ...   Up      6379/tcp
stackdemo_web_1     python app.py                    Up      0.0.0.0:8000->8000/tcp
vagrant@manager01:~$ curl http://localhost:8000
Hello World! I have been seen 1 times.
vagrant@manager01:~$ curl http://localhost:8000
Hello World! I have been seen 2 times.
vagrant@manager01:~$ curl http://localhost:8000
Hello World! I have been seen 3 times.
vagrant@manager01:~$

vagrant@manager01:~$ docker-compose -f /vagrant/stackdemo/docker-compose.yml down --volumes
Stopping stackdemo_redis_1 ... done                                                                                                                                                                                Stopping stackdemo_web_1   ... done                                                                                                                                                                                Removing stackdemo_redis_1 ... done                                                                                                                                                                                Removing stackdemo_web_1   ... done                                                                                                                                                                                Removing network stackdemo_default
vagrant@manager01:~

vagrant@manager01:~$ docker-compose -f /vagrant/stackdemo/docker-compose.yml push
Pushing web (127.0.0.1:5000/stackdemo:latest)...
The push refers to a repository [127.0.0.1:5000/stackdemo]
d8257afc28b3: Pushed                                                                                                                                                                                               3b722aa46af5: Pushed                                                                                                                                                                                               46ed3d879948: Pushed                                                                                                                                                                                               fbeeb71995b3: Pushed                                                                                                                                                                                               bb9e1c111e49: Pushed                                                                                                                                                                                               ac3ac7a153b5: Pushed                                                                                                                                                                                               3bfeb766f97b: Pushed                                                                                                                                                                                               ea1227feeccb: Pushed                                                                                                                                                                                               9cae1895156d: Pushed                                                                                                                                                                                               52dba9daa22c: Pushed                                                                                                                                                                                               78c1b9419976: Pushed                                                                                                                                                                                               latest: digest: sha256:128e6f9da4fcd3776864d2a5421ae2e62aa00031fd1100ea7b1238a28b41ff31 size: 2636
vagrant@manager01:~

vagrant@manager01:~$ docker stack deploy --compose-file /vagrant/stackdemo/docker-compose.yml stackdemo
Ignoring unsupported options: build

Creating network stackdemo_default
Creating service stackdemo_web
Creating service stackdemo_redis
vagrant@manager01:~$ docker stack services stackdemo
ID                  NAME                MODE                REPLICAS            IMAGE                             PORTS
1if7z7rqyiwh        stackdemo_redis     replicated          0/1                 redis:alpine
e4ngeufefa1k        stackdemo_web       replicated          1/1                 127.0.0.1:5000/stackdemo:latest   *:8000->8000/tcp
vagrant@manager01:~$

vagrant@manager01:~$ curl http://localhost:8000
Hello World! I have been seen 1 times.
vagrant@manager01:~$ curl http://localhost:8000
Hello World! I have been seen 2 times.
vagrant@manager01:~$ curl http://localhost:8000
Hello World! I have been seen 3 times.
vagrant@manager01:~$


vagrant@manager01:~$ docker stack rm stackdemo
Removing service stackdemo_redis
Removing service stackdemo_web
Removing network stackdemo_default
vagrant@manager01:~$ docker service rm registry
registry
~~~
~~~
Deploy a stack to a swarm
https://docs.docker.com/engine/swarm/stack-deploy/
~~~
