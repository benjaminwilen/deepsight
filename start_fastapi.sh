#!/bin/bash

# Set the default values
HOST="127.0.0.1"
PORT="8000"
RELOAD="true"

# Parse command-line arguments
while [[ "$#" -gt 0 ]]; do
    case $1 in
        --host) HOST="$2"; shift ;;
        --port) PORT="$2"; shift ;;
        --reload) RELOAD="true" ;;
        *) echo "Unknown parameter passed: $1"; exit 1 ;;
    esac
    shift
done

# Construct the uvicorn command
COMMAND="uvicorn api.rest_apis:app --host $HOST --port $PORT"
if [ "$RELOAD" = "true" ]; then
    COMMAND="$COMMAND --reload"
fi

# Run the command
echo "Starting FastAPI with command: $COMMAND"
$COMMAND