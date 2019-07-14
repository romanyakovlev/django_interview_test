# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from . import views
from .site_parser import get_new_info, start_parsing

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^start_parsing/', start_parsing),
    url(r'^get_new_info/', get_new_info),
]
