# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-07-01 08:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sm_user', '0017_auto_20190701_0838'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stockmarket',
            name='created',
        ),
    ]
