# -*- coding:utf-8 -*-
from django.conf.urls import url
import views

app_name = 'tips'
urlpatterns = [
    url(r'^index/$', views.index, name='index'),
]