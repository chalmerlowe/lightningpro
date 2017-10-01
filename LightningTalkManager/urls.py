from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^manager/', include('manager.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/manager/'}, name='logout'),
]
