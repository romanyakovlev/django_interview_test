# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class SiteAdminModel(models.Model):

    site_url = models.URLField(blank=False)
    site_title = models.CharField(max_length=200, blank=True, null=True)
    site_header = models.CharField(max_length=200, blank=True, null=True)
    parsing_complete = models.BooleanField(default=False)
    timeshift_for_parsing = models.PositiveIntegerField(default=0)
    parsing_time = models.DateTimeField(null=True)

    class Meta:
        verbose_name = 'сайт для парсинга'
