# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-20 19:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('parse_app', '0002_auto_20160920_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
