# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-13 17:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites_parser', '0003_auto_20190712_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteadminmodel',
            name='site_encoding',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='siteadminmodel',
            name='site_header',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='siteadminmodel',
            name='site_title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
