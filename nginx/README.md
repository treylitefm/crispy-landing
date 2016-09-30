# Nginx

This docker image is meant to be used as a base template for deploying an nginx proxy for use in conjunction with an app running in another container.

An important thing to note: when a container is created using the --link [another-container-name] flag, it is added to the /etc/hosts file of the newly created contiainer. This allows us to easily reference the host name from nginx.conf with a short and sweet alias such as 

```
http://[linked-containers-name]:[port-number]
```

in a similar to fashion to how localhost is defined in /etc/hosts and always resolves to 127.0.0.1.

