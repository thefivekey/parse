# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-20 17:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parse_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='content',
        ),
        migrations.AddField(
            model_name='page',
            name='first_h1',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='first_img',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
