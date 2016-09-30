FROM ubuntu:trusty
MAINTAINER treylitefm

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y python python-pip
RUN apt-get install -y default-jre #200+MB download :/

RUN pip install --upgrade pip
RUN pip install flask flask-bcrypt flask-cors 

RUN pip install selenium browsermob-proxy supervisor rq

#EXPOSE 5000

WORKDIR /var/monitor
COPY docker-entrypoint.sh /

VOLUME ["/var/monitor"]

ENTRYPOINT ["/docker-entrypoint.sh", "redis-server"]
