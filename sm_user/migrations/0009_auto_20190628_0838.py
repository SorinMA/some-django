# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-28 08:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sm_user', '0008_remove_stockexpert_email_confirmed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stockmarket',
            old_name='stock_evolution',
            new_name='stock_CHF',
        ),
        migrations.AddField(
            model_name='stockmarket',
            name='stock_RON',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='stockmarket',
            name='stock_USD',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='stockmarket',
            name='stock_msg',
            field=models.CharField(default='', max_length=255),
        ),
    ]