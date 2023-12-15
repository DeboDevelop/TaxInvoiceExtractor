#!/bin/bash

if [ -f .env ]; then
    export $(cat .env | grep -v '^#' | xargs)
fi

POSTGRES_CONTAINER_NAME="my_postgres"
POSTGRES_USER="${POSTGRES_USER:-your_default_username}"
POSTGRES_PASSWORD="${POSTGRES_PASSWORD:-your_default_password}"
POSTGRES_DB="${POSTGRES_DB:-your_default_database}"
POSTGRES_PORT="${POSTGRES_PORT:-5432}"

if [ "$(docker ps -q -f name=$POSTGRES_CONTAINER_NAME)" ]; then
    # Restart the PostgreSQL container
    docker restart $POSTGRES_CONTAINER_NAME
    echo "PostgreSQL container restarted."
else
    # Run the PostgreSQL container
    docker run -d \
        --name $POSTGRES_CONTAINER_NAME \
        -p 5432:5432 \
        -e POSTGRES_USER=your_default_username \
        -e POSTGRES_PASSWORD=your_default_password \
        -e POSTGRES_DB=your_default_database \
        postgres

    echo "PostgreSQL container started."
fi
