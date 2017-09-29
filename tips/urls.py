# -*- coding:utf-8 -*-
from django.conf.urls import url
import views

app_name = 'tips'
urlpatterns = [
    url(r'^lists/$', views.ListsView.as_view(), name='lists'),
]
