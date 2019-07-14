# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import SiteAdminModel


def index(request):

    return render(request, 'sites_parser/index.html', {'sites': SiteAdminModel.objects.all()})
