#! /bin/bash

CONTAINERS="$(docker ps | grep digits | cut -f1 -d' ')" ;
[ -z ${CONTAINERS} ] && docker kill "${CONTAINERS}" ;
docker build --tag digits . ;
docker run --tty digits ;
