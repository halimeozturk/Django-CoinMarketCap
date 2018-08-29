from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from .models import Cryptocurrency,Value
from django.db.models import OuterRef, Subquery

def get_main(request):

    data = []
    newest_value = Value.objects.filter(cryptocurrency=OuterRef('pk')).order_by('-last_updated')
    currencies = Cryptocurrency.objects.annotate(
        newest_price=Subquery(newest_value.values('price')[:1]),
        newest_percent_change_1h=Subquery(newest_value.values('percent_change_1h')[:1]),
        newest_percent_change_24h=Subquery(newest_value.values('percent_change_24h')[:1]),
        newest_percent_change_7d=Subquery(newest_value.values('percent_change_7d')[:1]),
        newest_market_cap=Subquery(newest_value.values('market_cap')[:1]),
        newest_last_updated=Subquery(newest_value.values('last_updated')[:1])
    )
    
    for currency in currencies:
        data.append(
            {
                'name': currency.name,
                'price': currency.newest_price,
                'percent_change_1h': currency.newest_percent_change_1h,
                'percent_change_24h': currency.newest_percent_change_24h,
                'percent_change_7d': currency.newest_percent_change_7d,
                'market_cap': currency.newest_market_cap,
                'last_updated': currency.newest_last_updated

            }
        )

    # import ipdb; ipdb.set_trace()

    return JsonResponse(data, safe=False)