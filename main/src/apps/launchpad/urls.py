from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^apps/(?P<app_id>\d+)', views.show_app, name='show_app'),
    url(r'^', views.index, name='index'),
]
