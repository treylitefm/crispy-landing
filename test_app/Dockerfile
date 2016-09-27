FROM ubuntu:trusty
MAINTAINER treylitefm

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y python python-pip supervisor redis-tools 

RUN pip install --upgrade pip
RUN pip install flask flask-bcrypt flask-cors rq

EXPOSE 5000

WORKDIR /var/test_app
VOLUME ["/var/test_app"]
