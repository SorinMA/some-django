# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class StockExpert(models.Model):
    stock_player = models.ForeignKey(User, related_name="stock_player")
    last_active = models.DateTimeField(auto_now=True)
    stock_player_revenue = models.FloatField()

class StockMarket(models.Model):
    stock_evolution = models.FloatField(null=False, default=0)
    stock_expert_player = models.ForeignKey(StockExpert, on_delete=models.CASCADE)

