#!/bin/bash

POSTGRES_CONTAINER_NAME="my_postgres"

# Check if the container is running
if [ "$(docker ps -q -f name=$POSTGRES_CONTAINER_NAME)" ]; then
    docker stop $POSTGRES_CONTAINER_NAME 2>/dev/null
    docker rm $POSTGRES_CONTAINER_NAME 2>/dev/null
    echo "PostgreSQL container stopped."
else
    echo "PostgreSQL container is not running."
fi
