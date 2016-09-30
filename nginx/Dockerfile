FROM nginx
MAINTAINER treylitefm

WORKDIR /etc/nginx/

COPY nginx.conf.template  /etc/nginx/nginx.conf.template
COPY generate_conf.sh     /etc/nginx/generate_conf.sh
RUN ./generate_conf.sh -a hermes -p 8000 -s localhost
RUN mv nginx-hermes.conf nginx.conf

COPY static  /var/www/static/
