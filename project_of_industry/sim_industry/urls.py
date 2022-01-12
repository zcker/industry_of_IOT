#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2022-1-10 上午 11:22
# Author:ZhangChengkai
# @File    : urls.py
from django.urls import path
from django.conf.urls import include, url
from sim_industry import views

urlpatterns = [
    path('weight/', views.weight_info),
    path('gas/',views.gas_info),
    path('temperature/',views.temperature_info),
    path('index/',views.index_info),
    path('door/',views.door_info),
    path('fire/',views.fire_info),
    path('water/',views.water_info),
    path('play/',views.play),
    path('pause/',views.pause)
]