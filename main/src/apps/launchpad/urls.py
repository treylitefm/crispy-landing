from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^pages/new/(?P<app_id>\d+)', views.new_page, name='new_page'),
    url(r'^pages/edit/(?P<page_id>\d+)', views.edit_page, name='edit_page'),
    url(r'^pages/(?P<page_id>\d+)', views.show_page, name='show_page'),
    url(r'^apps/new', views.new_app, name='new_app'),
    url(r'^apps/(?P<app_id>\d+)/pages/(?P<page_id>\d+)', views.show_page, name='show_page'),
    url(r'^apps/(?P<app_id>\d+)', views.show_app, name='show_app'),
    url(r'^$', views.index, name='index'),
]
