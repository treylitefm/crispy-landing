from django.conf.urls import include,url
from django.contrib import admin

from django.contrib.auth import views
from forms.auth_forms import LoginForm

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^logout/$', views.logout, {'next_page': '/login/'}, name='logout'), 
    url(r'^login/$', views.login, {'template_name': 'login.html', 'authentication_form': LoginForm }, name='login'), 
    url(r'^', include('apps.launchpad.urls', namespace='launchpad')),
    url(r'^$', views.login, {'template_name': 'login.html', 'authentication_form': LoginForm }, name='index'), 
]
