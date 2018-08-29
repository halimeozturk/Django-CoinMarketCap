# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from decimal import *



class Cryptocurrency(models.Model):
    name = models.CharField(null=True, max_length=25)
    symbol = models.CharField(null=True, max_length=25)

    def __str__(self):
        return self.name

class Value(models.Model):
    cryptocurrency = models.ForeignKey(Cryptocurrency, on_delete=models.CASCADE)
    price = models.DecimalField(null=True, max_digits=15, decimal_places=5)
    percent_change_1h = models.DecimalField(null=True, max_digits=15, decimal_places=5)
    percent_change_24h = models.DecimalField(null=True, max_digits=15, decimal_places=5)
    percent_change_7d = models.DecimalField(null=True, max_digits=15, decimal_places=5)
    market_cap = models.DecimalField(null=True, max_digits=25, decimal_places=5)
    last_updated = models.DateTimeField(null=True, max_length=25)

    def __str__(self):
        return self.cryptocurrency.name

    





