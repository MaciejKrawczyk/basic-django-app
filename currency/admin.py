from django.contrib import admin
from django.shortcuts import render

from .models import Currency, ExchangeRate
import yfinance as yf


admin.site.register(Currency)
admin.site.register(ExchangeRate)


def historical_rates(request, id):

    data_from_database = ExchangeRate.objects.filter(id=id)

    data_from_yf = (yf.Ticker(f"{data_from_database[0].from_currency.code}{data_from_database[0].to_currency.code}" + "=X")
                    .history(period="6mo"))  # todo need to fetch this from my database (?)

    return render(request, 'admin/historical_rates.html', {'data_from_yf': data_from_yf})
