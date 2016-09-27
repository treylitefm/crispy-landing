from __future__ import unicode_literals

from django.db import models

class App(models.Model):
    name = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'apps'

class Page(models.Model):
    url = models.CharField(max_length=255)
    app = models.ForeignKey(App)
#    status = models.
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'pages'

class TestRun(models.Model):
    pass
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
