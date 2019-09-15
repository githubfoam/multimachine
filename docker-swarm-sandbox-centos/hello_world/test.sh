#!/bin/bash
sleep 5
WEB_APP_IP=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' hello_world_web_1)
#if curl http://${WEB_APP_IP}:80 | grep -q '<b>Visits:</b>' ; then
if curl http://172.17.0.3:80 | grep -q '<b>Visits:</b>' ; then
  echo "Tests passed!"
  exit 0
else
  echo "Tests failed!"
  exit 1
fi
