# docker deployment; envoy

~~~~
$ sudo docker pull envoyproxy/envoy-dev:817b2e36689cbc9e32892fc53f253f8e6361d5dd

$ sudo docker image ls
REPOSITORY                 TAG                                        IMAGE ID            CREATED             SIZE
envoyproxy/envoy-dev       817b2e36689cbc9e32892fc53f253f8e6361d5dd   83b6bd0577e9        2 days ago          151MB

$ sudo  docker run --rm -d -p 10000:10000 envoyproxy/envoy-dev:817b2e36689cbc9e32892fc53f253f8e6361d5dd

$ sudo docker container ls
CONTAINER ID        IMAGE                                                           COMMAND                  CREATED             STATUS              PORTS                      NAMES
0818ab5f2704        envoyproxy/envoy-dev:817b2e36689cbc9e32892fc53f253f8e6361d5dd   "/docker-entrypoint.…"   5 minutes ago       Up 5 minutes        0.0.0.0:10000->10000/tcp   epic_driscoll

$ curl -v 192.168.45.41:10000
~~~~
~~~~
Quick Start to Run Simple Example
https://www.envoyproxy.io/docs/envoy/latest/start/start
~~~~
