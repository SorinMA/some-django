# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-28 10:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sm_user', '0013_auto_20190628_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockmarket',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 28, 10, 34, 46, 470135)),
        ),
    ]
