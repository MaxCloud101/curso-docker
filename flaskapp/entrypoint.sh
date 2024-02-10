#!/bin/bash
echo "Starting my application..."

if [ $SERVER_ENV = 'production' ]; then
  echo "RUNNING: production mode"
else
  echo "RUNNING: development mode"
fi;

exec "$@"