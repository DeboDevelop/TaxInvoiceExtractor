#!/bin/bash

# Get the directory of the script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Navigate two directories up to find the .env file
ENV_FILE="$SCRIPT_DIR/../../.env"

# Load environment variables from .env file
if [ -f "$ENV_FILE" ]; then
    source "$ENV_FILE"
    echo "Environment variables loaded from $ENV_FILE"
else
    echo "Error: $ENV_FILE not found"
    exit 1
fi

POSTGRES_CONTAINER_NAME="my_postgres"

if [ "$(docker ps -q -f name=$POSTGRES_CONTAINER_NAME)" ]; then
    # Restart the PostgreSQL container
    docker restart $POSTGRES_CONTAINER_NAME
    echo "PostgreSQL container restarted."
else
    # Run the PostgreSQL container
    docker run -d \
        --name $POSTGRES_CONTAINER_NAME \
        -p 5433:5432 \
        -e POSTGRES_USER=$POSTGRES_USER \
        -e POSTGRES_PASSWORD=$POSTGRES_PASSWORD \
        -e POSTGRES_DB=$POSTGRES_DB \
        postgres

    echo "PostgreSQL container started."
fi
