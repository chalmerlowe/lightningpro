from django.conf.urls import url
from . import views

app_name = 'manager'

urlpatterns = [
	url(r'^loginredirect/$', views.login_redirect, name='login_redirect'),
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^addtalk/$', views.addtalk, name='addtalk'),
	url(r'^$', views.index, name='index'),
]