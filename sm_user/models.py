# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

from django.utils import timezone

import datetime
# Create your models here.



class StockExpert(models.Model):
    stock_player = models.OneToOneField(User, related_name="stock_player", on_delete=models.CASCADE)
    stock_player_revenue = models.FloatField()



class StockMarket(models.Model):
    stock_RON = models.FloatField(null=False, default=0)
    stock_USD = models.FloatField(null=False, default=0)
    stock_CHF = models.FloatField(null=False, default=0)
    stock_msg = models.CharField(max_length=255, default="")
    stock_moment = models.CharField(max_length=30, default="--/--/--");
    stock_expert_player = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return '%s - %s - %s - %s - %s' % (self.stock_RON, self.stock_USD, self.stock_CHF, self.stock_msg, self.stock_moment)
    def get_RON(self):
        return self.stock_RON
    def get_USD(self):
        return self.stock_USD
    def get_CHF(self):
        return self.stock_CHF
    def get_msg(self):
        return self.stock_msg
    def get_moment(self):
        return self.stock_moment

