from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

DEFAULT_OWNER_ID = 1

PROTOCOLS = (
    (0, 'http'),
    (1, 'https')
)

SEVERITIES = (
    (1, 'Green'),
    (3, 'Yellow'),
    (5, 'Red')
)

class App(models.Model):
    name = models.CharField(max_length=255, default='')
    domain = models.CharField(max_length=255, default='')
    protocol = models.SmallIntegerField(choices=PROTOCOLS, default=0)
    owner = models.ForeignKey(User, default=DEFAULT_OWNER_ID)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'apps'

class Page(models.Model):
    path = models.CharField(max_length=255, default='/')
    app = models.ForeignKey(App)
    ping_health = models.SmallIntegerField(default=1, choices=SEVERITIES)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'pages'

class TestRun(models.Model):
    page = models.ForeignKey(Page)
    status = models.SmallIntegerField(default=1, choices=SEVERITIES)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'test_runs'

'''
class Session():
    pass
class Down():
    pass
class Alert():
    pass
class Type():
    pass
'''
