from django.conf.urls import url
from . import views

# TEMPLATE TAGGING
APP_NAME = 'basic_app_name'

urlpatterns = [
    url(r'^relative/$', views.relative, name='relative'),
    url(r'^other/$', views.other, name='other'),
]
