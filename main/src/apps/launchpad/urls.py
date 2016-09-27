from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^pages/(?P<page_id>\d+)', views.show_page, name='show_page'),
    url(r'^apps/(?P<app_id>\d+)', views.show_app, name='show_app'),
    url(r'^$', views.index, name='index'),
]