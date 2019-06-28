# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

from django.db.models.signals import post_save

from django.dispatch import receiver
# Create your models here.

class StockExpert(models.Model):
    stock_player = models.OneToOneField(User, related_name="stock_player", on_delete=models.CASCADE)
    stock_player_revenue = models.FloatField()



class StockMarket(models.Model):
    stock_RON = models.FloatField(null=False, default=0)
    stock_USD = models.FloatField(null=False, default=0)
    stock_CHF = models.FloatField(null=False, default=0)
    stock_msg = models.CharField(max_length=255, default="")
    stock_expert_player = models.ForeignKey(StockExpert, on_delete=models.CASCADE)

