#!/bin/bash

redis-cli -h $1 keys "*" > /dev/null

while [ $? -eq 1 ]; do
    echo Database not ready for connections
    echo Sleeping 3 seconds then trying again...
    sleep 3
    redis-cli -h $1 keys "*" > /dev/null
done

echo Database is ready bub
sleep 3

/usr/local/bin/supervisord -n -c /var/monitor/supervisord.conf
