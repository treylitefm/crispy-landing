from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

DEFAULT_OWNER_ID = 1

PROTOCOLS = (
    (0, 'http'),
    (1, 'https')
)

class App(models.Model):
    name = models.CharField(max_length=255, default='')
    domain = models.CharField(max_length=255, default='')
    protocol = models.SmallIntegerField(choices=PROTOCOLS, default=0)
    owner = models.ForeignKey(User, default=DEFAULT_OWNER_ID)
    enabled = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'apps'

class Page(models.Model):
    path = models.CharField(max_length=255, default='/')
    app = models.ForeignKey(App)
    enabled = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'pages'

