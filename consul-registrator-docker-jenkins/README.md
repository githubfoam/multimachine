# docker deployment; consul - registrator -  microservices

~~~~
run in the background without UI
sudo docker run -p 8400:8400 -p 8500:8500 -p 8600:53/udp -h node1 progrium/consul -server -bootstrap &
~~~~
~~~~

run in the background with UI
sudo docker run -p 8400:8400 -p 8500:8500 -p 8600:53/udp -h node1 progrium/consul -server -bootstrap -ui-dir /ui &

http://192.168.45.41:8500/ui

access Consul's HTTP API via the Docker machine's IP
$ curl 192.168.45.41:8500/v1/catalog/services
{"consul":[]}

On Node1
$ sudo docker run -d --name node1 -h node1 progrium/consul -server -bootstrap-expect 3 &
[2] 18201

-bootstrap-expect 3 means that the consul server will wait until there are 3 peers connected before self-bootstrapping and becoming a working cluster.

$ sudo docker inspect -f '{{.NetworkSettings.IPAddress}}' node1
172.17.0.3

$ export JOIN_IP="172.17.0.3"
$ echo $JOIN_IP
172.17.0.3

On Node2
$ sudo docker run -d --name node2 -h node2 progrium/consul -server -join $JOIN_IP
6ba9fc54cabba3fcbec63e1c3e4709f72f1601f8147f8b7d34bd6836b87009a0

On Node3
$ sudo docker run -d --name node3 -h node3 progrium/consul -server -join $JOIN_IP
76b044f2811999e981097e161a822bb1b9c0e2dab226e210d858842354754991

Building Registrator for Service Discovery


sudo docker run -d \
    --name=registrator \
    --net=host \
    --volume=/var/run/docker.sock:/tmp/docker.sock \
    gliderlabs/registrator:latest \
      consul://192.168.45.41:8500

      $ sudo docker logs registrator
      2019/08/19 19:09:41 Starting registrator v7 ...
      2019/08/19 19:09:41 Using consul adapter: consul://192.168.45.41:8500
      2019/08/19 19:09:41 Connecting to backend (0/0)
      2019/08/19 19:09:41 consul: current leader  172.17.0.2:8300
~~~~

deploy jenkins
~~~~

$ sudo docker run --name jenkinsci -p 8080:8080 jenkins/jenkins:lts

check on
http://192.168.45.41:8500/ui

jenkins IU
http://192.168.45.41:8080
~~~~

~~~~
Consul - Working with Microservices
https://www.tutorialspoint.com/consul/consul_working_with_microservices.htm
Quickstart
https://gliderlabs.com/registrator/latest/user/quickstart/
~~~~
