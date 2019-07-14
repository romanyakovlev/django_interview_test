# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import SiteAdminModel

class SiteAdmin(admin.ModelAdmin):

    list_display = ['site_url', 'timeshift_for_parsing']
    readonly_fields = ('parsing_time', 'site_title', 'site_header', 'parsing_complete', 'site_encoding')

admin.site.register(SiteAdminModel, SiteAdmin)
