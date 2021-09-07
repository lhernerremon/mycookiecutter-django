#!/usr/bin/sh
container_id=$(docker ps -aqf "name=django")
docker rm -f $container_id

docker-compose -f local.yml run  --rm --service-ports django
