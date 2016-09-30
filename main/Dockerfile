FROM ubuntu:trusty
MAINTAINER treylitefm

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y python python-pip libpq-dev python-dev

RUN pip install --upgrade pip
RUN pip install psycopg2==2.6.2 Django==1.10.1 bcrypt==3.1.1 gunicorn==19.6.0

EXPOSE 8000

WORKDIR /var/hermes
VOLUME ["/var/hermes"]

COPY ./docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh", "hermes"]
