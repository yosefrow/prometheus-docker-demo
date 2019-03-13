#!/bin/bash -xe

ScriptDir=$(dirname $0)
cd $ScriptDir

if [ ! -f ./.env ]; then
    echo ".env file not found. Copying .env.example to .env"
    cp -i .env.example .env
fi

docker-compose down
docker-compose up -d
