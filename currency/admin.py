from django.contrib import admin
from django.shortcuts import render

from .models import Currency, ExchangeRate, ExchangeRateHistory


admin.site.register(Currency)
admin.site.register(ExchangeRate)
# admin.site.register(ExchangeRateHistory)


def historical_rates(request, id):

    data_from_database = ExchangeRate.objects.get(id=id)

    currency_from = data_from_database.from_currency.code
    currency_to = data_from_database.to_currency.code
    currency_pair = currency_from + currency_to

    data_from_yf = ExchangeRateHistory.objects.filter(currency_pair_history=id)

    return render(request, 'admin/historical_rates.html', {'data_from_yf': data_from_yf, 'currency_pair': currency_pair})
