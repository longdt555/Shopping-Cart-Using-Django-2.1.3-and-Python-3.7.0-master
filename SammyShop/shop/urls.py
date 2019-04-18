from django.conf.urls import url
from . import views

app_name='shop'

urlpatterns=[
    url(r'^$', views.home, name='homepage'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^register/$', views.user_register, name='register'),
]
