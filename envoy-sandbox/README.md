
# envoy sandbox

~~~~
$ envoy --config-path ./basic-front-proxy.yaml

# shell window-2
$ curl -s -o /dev/null -vvv -H 'Host: google.com' localhost:15000
$ curl -vvv -H 'Host: google.com' localhost:15000
$ curl -vvv -H 'Host: bing.com' localhost:15000
$ curl -s -o /dev/null -vvv -H 'Host: bing.com' localhost:15000

# shell window-1
$ envoy --config-path ./basic-front-proxy.yaml
[2019-08-19 17:06:19.338][6820][info][main] [external/envoy/source/server/server.cc:240] initializing epoch 0 (hot restart version=11.104)
[2019-08-19 17:06:19.338][6820][info][main] [external/envoy/source/server/server.cc:242] statically linked extensions:
[2019-08-19 17:06:19.338][6820][info][main] [external/envoy/source/server/server.cc:244]   access_loggers: envoy.file_access_log,envoy.http_grpc_access_log
[2019-08-19 17:06:19.338][6820][info][main] [external/envoy/source/server/server.cc:247]   filters.http: envoy.buffer,envoy.cors,envoy.csrf,envoy.ext_authz,envoy.fault,envoy.filters.http.dynamic_forward_proxy,envoy.filters.http.grpc_http1_reverse_bridge,envoy.filters.http.header_to_metadata,envoy.filters.http.jwt_authn,envoy.filters.http.original_src,envoy.filters.http.rbac,envoy.filters.http.tap,envoy.grpc_http1_bridge,envoy.grpc_json_transcoder,envoy.grpc_web,envoy.gzip,envoy.health_check,envoy.http_dynamo_filter,envoy.ip_tagging,envoy.lua,envoy.rate_limit,envoy.router,envoy.squash
[2019-08-19 17:06:19.338][6820][info][main] [external/envoy/source/server/server.cc:250]   filters.listener: envoy.listener.http_inspector,envoy.listener.original_dst,envoy.listener.original_src,envoy.listener.proxy_protocol,envoy.listener.tls_inspector
[2019-08-19 17:06:19.338][6820][info][main] [external/envoy/source/server/server.cc:253]   filters.network: envoy.client_ssl_auth,envoy.echo,envoy.ext_authz,envoy.filters.network.dubbo_proxy,envoy.filters.network.mysql_proxy,envoy.filters.network.rbac,envoy.filters.network.sni_cluster,envoy.filters.network.thrift_proxy,envoy.filters.network.zookeeper_proxy,envoy.http_connection_manager,envoy.mongo_proxy,envoy.ratelimit,envoy.redis_proxy,envoy.tcp_proxy
[2019-08-19 17:06:19.338][6820][info][main] [external/envoy/source/server/server.cc:255]   stat_sinks: envoy.dog_statsd,envoy.metrics_service,envoy.stat_sinks.hystrix,envoy.statsd
[2019-08-19 17:06:19.338][6820][info][main] [external/envoy/source/server/server.cc:257]   tracers: envoy.dynamic.ot,envoy.lightstep,envoy.tracers.datadog,envoy.tracers.opencensus,envoy.zipkin
[2019-08-19 17:06:19.338][6820][info][main] [external/envoy/source/server/server.cc:260]   transport_sockets.downstream: envoy.transport_sockets.alts,envoy.transport_sockets.tap,raw_buffer,tls
[2019-08-19 17:06:19.338][6820][info][main] [external/envoy/source/server/server.cc:263]   transport_sockets.upstream: envoy.transport_sockets.alts,envoy.transport_sockets.tap,raw_buffer,tls
[2019-08-19 17:06:19.338][6820][info][main] [external/envoy/source/server/server.cc:269] buffer implementation: new
[2019-08-19 17:06:19.343][6820][info][main] [external/envoy/source/server/server.cc:324] admin address: 0.0.0.0:15001
[2019-08-19 17:06:19.345][6820][info][main] [external/envoy/source/server/server.cc:438] runtime: layers:
  - name: base
    static_layer:
      {}
  - name: admin
    admin_layer:
      {}
[2019-08-19 17:06:19.345][6820][info][config] [external/envoy/source/server/configuration_impl.cc:62] loading 0 static secret(s)
[2019-08-19 17:06:19.345][6820][info][config] [external/envoy/source/server/configuration_impl.cc:68] loading 2 cluster(s)
[2019-08-19 17:06:19.349][6820][info][config] [external/envoy/source/server/configuration_impl.cc:72] loading 1 listener(s)
[2019-08-19 17:06:19.351][6820][info][config] [external/envoy/source/server/configuration_impl.cc:97] loading tracing configuration
[2019-08-19 17:06:19.351][6820][info][config] [external/envoy/source/server/configuration_impl.cc:117] loading stats sink configuration
[2019-08-19 17:06:19.351][6820][info][main] [external/envoy/source/server/server.cc:523] starting main dispatch loop
[2019-08-19 17:06:19.363][6820][info][upstream] [external/envoy/source/common/upstream/cluster_manager_impl.cc:147] cm init: all clusters initialized
[2019-08-19 17:06:19.363][6820][info][main] [external/envoy/source/server/server.cc:506] all clusters initialized. initializing init manager
[2019-08-19 17:06:19.363][6820][info][config] [external/envoy/source/server/listener_manager_impl.cc:775] all dependencies initialized. starting workers
[2019-08-19T17:08:35.922Z] "GET / HTTP/1.1" 200 - 0 12070 189 176 "-" "curl/7.29.0" "0f058523-8a24-4812-91d6-edc4117e8bc3" "www.google.com" "172.217.17.164:80"
[2019-08-19T17:08:57.997Z] "GET / HTTP/1.1" 200 - 0 12053 198 170 "-" "curl/7.29.0" "691fcd74-2466-4298-854b-fee449b7ec65" "www.google.com" "172.217.17.164:80"
[2019-08-19T17:09:32.918Z] "GET / HTTP/1.1" 200 - 0 91030 356 231 "-" "curl/7.29.0" "ffbf9e16-84ea-4e08-b2d6-416f58442967" "www.bing.com" "204.79.197.200:80"
[2019-08-19T17:09:44.291Z] "GET / HTTP/1.1" 200 - 0 91030 242 179 "-" "curl/7.29.0" "6d99e440-0b23-408a-b5e6-3d414dc3842a" "www.bing.com" "204.79.197.200:80"


~~~~
