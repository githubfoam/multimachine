
# etcd sandbox

~~~~
vagrant up etcd1
vagrant up etcd2
vagrant up etcd3

sudo systemctl start etcd
sudo systemctl status etcd -l 
~~~~

~~~~
agrant@etcd1:~$ systemctl status etcd -l
● etcd.service - etcd service
   Loaded: loaded (/etc/systemd/system/etcd.service; enabled; vendor preset: enabled)
   Active: active (running) since Sat 2019-08-17 18:57:43 UTC; 8min ago
     Docs: https://github.com/etcd-io/etcd
 Main PID: 14770 (etcd)
    Tasks: 9 (limit: 1134)
   Memory: 20.6M
   CGroup: /system.slice/etcd.service
           └─14770 /usr/local/bin/etcd --name etcd1 --data-dir=/var/lib/etcd --initial-advertise-peer-urls http://192.168.18.9:2380 --listen-peer-urls http://192.168.18.9:2380 --listen-client-urls http://192.168

Aug 17 19:03:22 etcd1 etcd[14770]: health check for peer 152d6f8123c6ac97 could not connect: dial tcp 192.168.18.11:2380: connect: connection refused (prober "ROUND_TRIPPER_RAFT_MESSAGE")
Aug 17 19:03:22 etcd1 etcd[14770]: health check for peer 152d6f8123c6ac97 could not connect: dial tcp 192.168.18.11:2380: connect: connection refused (prober "ROUND_TRIPPER_SNAPSHOT")
Aug 17 19:03:22 etcd1 etcd[14770]: peer 152d6f8123c6ac97 became active
Aug 17 19:03:22 etcd1 etcd[14770]: established a TCP streaming connection with peer 152d6f8123c6ac97 (stream MsgApp v2 reader)
Aug 17 19:03:22 etcd1 etcd[14770]: established a TCP streaming connection with peer 152d6f8123c6ac97 (stream Message reader)
Aug 17 19:03:22 etcd1 etcd[14770]: established a TCP streaming connection with peer 152d6f8123c6ac97 (stream Message writer)
Aug 17 19:03:22 etcd1 etcd[14770]: established a TCP streaming connection with peer 152d6f8123c6ac97 (stream MsgApp v2 writer)
Aug 17 19:03:23 etcd1 etcd[14770]: updating the cluster version from 3.0 to 3.3
Aug 17 19:03:23 etcd1 etcd[14770]: updated the cluster version from 3.0 to 3.3
Aug 17 19:03:23 etcd1 etcd[14770]: enabled capabilities for version 3.3
~~~~

~~~~
vagrant@etcd1:~$ etcdctl member list
152d6f8123c6ac97: name=etcd3 peerURLs=http://etcd3:2380 clientURLs=http://192.168.18.11:2379 isLeader=false
332a8a315e569778: name=etcd2 peerURLs=http://etcd2:2380 clientURLs=http://192.168.18.10:2379 isLeader=false
aebb404b9385ccd4: name=etcd1 peerURLs=http://etcd1:2380 clientURLs=http://192.168.18.9:2379 isLeader=true

vagrant@etcd2:~$ etcdctl member list
152d6f8123c6ac97: name=etcd3 peerURLs=http://etcd3:2380 clientURLs=http://192.168.18.11:2379 isLeader=false
332a8a315e569778: name=etcd2 peerURLs=http://etcd2:2380 clientURLs=http://192.168.18.10:2379 isLeader=false
aebb404b9385ccd4: name=etcd1 peerURLs=http://etcd1:2380 clientURLs=http://192.168.18.9:2379 isLeader=true

vagrant@etcd3:~$ etcdctl member list
152d6f8123c6ac97: name=etcd3 peerURLs=http://etcd3:2380 clientURLs=http://192.168.18.11:2379 isLeader=false
332a8a315e569778: name=etcd2 peerURLs=http://etcd2:2380 clientURLs=http://192.168.18.10:2379 isLeader=false
aebb404b9385ccd4: name=etcd1 peerURLs=http://etcd1:2380 clientURLs=http://192.168.18.9:2379 isLeader=true

vagrant@etcd2:~$ ETCDCTL_API=3 etcdctl member list
152d6f8123c6ac97, started, etcd3, http://etcd3:2380, http://192.168.18.11:2379
332a8a315e569778, started, etcd2, http://etcd2:2380, http://192.168.18.10:2379
aebb404b9385ccd4, started, etcd1, http://etcd1:2380, http://192.168.18.9:2379

vagrant@etcd2:~$ etcdctl member list
152d6f8123c6ac97: name=etcd3 peerURLs=http://etcd3:2380 clientURLs=http://192.168.18.11:2379 isLeader=false
332a8a315e569778: name=etcd2 peerURLs=http://etcd2:2380 clientURLs=http://192.168.18.10:2379 isLeader=false
aebb404b9385ccd4: name=etcd1 peerURLs=http://etcd1:2380 clientURLs=http://192.168.18.9:2379 isLeader=true

vagrant@etcd2:~$ etcdctl cluster-health
member 152d6f8123c6ac97 is healthy: got healthy result from http://192.168.18.11:2379
member 332a8a315e569778 is healthy: got healthy result from http://192.168.18.10:2379
member aebb404b9385ccd4 is healthy: got healthy result from http://192.168.18.9:2379
cluster is healthy

~~~~
~~~~
vagrant@etcd2:~$ etcdctl set /message "Hola Mundo"
Hola Mundo

vagrant@etcd2:~$ etcdctl get /message
Hola Mundo

vagrant@etcd2:~$ etcdctl mkdir /tmp/myservice
vagrant@etcd2:~$ etcdctl set /tmp/myservice/container1 localhost:8080
localhost:8080

vagrant@etcd2:~$ etcdctl ls /tmp/myservice
/tmp/myservice/container1
~~~~

~~~~

vagrant@etcd3:~$ etcdctl member list
152d6f8123c6ac97: name=etcd3 peerURLs=http://etcd3:2380 clientURLs=http://192.168.18.11:2379 isLeader=false
332a8a315e569778: name=etcd2 peerURLs=http://etcd2:2380 clientURLs=http://192.168.18.10:2379 isLeader=false
aebb404b9385ccd4: name=etcd1 peerURLs=http://etcd1:2380 clientURLs=http://192.168.18.9:2379 isLeader=true

vagrant@etcd1:~$ sudo systemctl stop etcd
vagrant@etcd1:~$ sudo systemctl status etcd
● etcd.service - etcd service
   Loaded: loaded (/etc/systemd/system/etcd.service; enabled; vendor preset: enabled)
   Active: inactive (dead) since Sat 2019-08-17 19:11:18 UTC; 4s ago
     Docs: https://github.com/etcd-io/etcd
  Process: 14770 ExecStart=/usr/local/bin/etcd --name etcd1 --data-dir=/var/lib/etcd --initial-advertise-peer-urls http://192.168.18.9:2380 --listen-peer-urls http://192.168.18.9:2380 --listen-client-urls http:/
 Main PID: 14770 (code=killed, signal=TERM)

Aug 17 19:11:18 etcd1 etcd[14770]: stopped peer 332a8a315e569778
Aug 17 19:11:18 etcd1 etcd[14770]: failed to find member 332a8a315e569778 in cluster 43f30402bb48a190
Aug 17 19:11:18 etcd1 etcd[14770]: failed to find member 152d6f8123c6ac97 in cluster 43f30402bb48a190
Aug 17 19:11:18 etcd1 etcd[14770]: failed to find member 152d6f8123c6ac97 in cluster 43f30402bb48a190
Aug 17 19:11:18 etcd1 etcd[14770]: failed to find member 332a8a315e569778 in cluster 43f30402bb48a190
Aug 17 19:11:18 etcd1 etcd[14770]: failed to find member 152d6f8123c6ac97 in cluster 43f30402bb48a190
Aug 17 19:11:18 etcd1 etcd[14770]: failed to find member 152d6f8123c6ac97 in cluster 43f30402bb48a190
Aug 17 19:11:18 etcd1 etcd[14770]: failed to find member 332a8a315e569778 in cluster 43f30402bb48a190
Aug 17 19:11:18 etcd1 etcd[14770]: failed to find member 332a8a315e569778 in cluster 43f30402bb48a190
Aug 17 19:11:18 etcd1 systemd[1]: Stopped etcd service.

vagrant@etcd3:~$ etcdctl member list
152d6f8123c6ac97: name=etcd3 peerURLs=http://etcd3:2380 clientURLs=http://192.168.18.11:2379 isLeader=false
332a8a315e569778: name=etcd2 peerURLs=http://etcd2:2380 clientURLs=http://192.168.18.10:2379 isLeader=true
aebb404b9385ccd4: name=etcd1 peerURLs=http://etcd1:2380 clientURLs=http://192.168.18.9:2379 isLeader=false
~~~~
