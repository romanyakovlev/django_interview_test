# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import SiteAdminModel

# Register your models here.

admin.site.register(SiteAdminModel)

class SiteAdminModel(admin.ModelAdmin):

    list_display = ["site_url", "timeshift_for_parsing", "parsing_complete"]
    readonly_fields = ('parsing_time', 'site_title', 'site_header')
