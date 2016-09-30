#!/bin/bash

while getopts "a:s:p:" opt; do
    case "$opt" in
        a)
            APP_NAME=$(echo $OPTARG | sed "s/https\{0,1\}:\/\///g" | sed "s/\///g" | sed "s/,/ /g")
            ;;
        s)
            SERVER_NAME=$(echo $OPTARG | sed "s/https\{0,1\}:\/\///g" | sed "s/\///g" | sed "s/,/ /g")
            ;;
        p)
            PORT=$(echo $OPTARG)
            ;;
    esac
done


if [ -z $APP_NAME ]; then
    echo App should not be blank
    exit 1
fi

if [ -z $PORT ]; then
    echo Port should not be blank
    exit 1
fi

echo APP NAME: $APP_NAME
echo PORT NUMBER: $PORT
echo SERVER NAME: $SERVER_NAME

cat nginx.conf.template | sed "s/\[app_name\]/${APP_NAME}/g" | sed "s/\[port_number\]/${PORT}/g" | sed "s/\[server_name\]/${SERVER_NAME}/g" > nginx-${APP_NAME}.conf

echo nginx-${APP_NAME}.conf generated!
