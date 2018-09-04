from django.core.management.base import BaseCommand, CommandError
from main.models import Cryptocurrency,Value
from django.shortcuts import render
from decimal import *
from ._api import *

class Command(BaseCommand):

    def handle(self,*args, **options):

        status , data = coins_data()

        for currency in data['data']:
            

            obj , created = Cryptocurrency.objects.get_or_create(
                name = currency['name'],
                symbol = currency['symbol'] 
            )

            usd = currency['quote']['USD']
            
            Value.objects.create(
                cryptocurrency = obj,
                price  = Decimal(usd['price']).quantize(Decimal('.0000')),
                percent_change_1h = Decimal(usd['percent_change_1h']).quantize(Decimal('.00001')),
                percent_change_24h = Decimal(usd['percent_change_24h']).quantize(Decimal('.0000')),
                percent_change_7d = Decimal(usd['percent_change_7d']).quantize(Decimal('.0000')),
                market_cap = Decimal(usd['market_cap']).quantize(Decimal('.0')),
                last_updated = usd['last_updated']
            )