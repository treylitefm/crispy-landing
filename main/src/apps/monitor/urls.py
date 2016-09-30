from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create/(?P<page_id>\d+)', views.new_test, name='new_test'),
    url(r'^update/(?P<test_id>\d+)', views.update_test, name='update_test'),
    url(r'^(?P<test_id>\d+)', views.index, name='index'),
]
