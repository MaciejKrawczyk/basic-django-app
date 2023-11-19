import os
from django.utils import timezone

import yfinance as yf
import json


def create_fixture():
    REQUIRED_CURRENCY_PAIRS = ["EURUSD", "USDJPY", "PLNUSD"]

    currencies_model_data_list = []
    exchange_rates_model_data_list = []

    def create_currency_model_data(code):
        return {
            "model": "currency.currency",
            "fields": {
                "code": code
            }
        }

    def create_exchange_rate_model_data(from_currency, to_currency, exchange_rate, currency, pk):
        return {
            "model": "currency.exchangerate",
            "pk": pk,
            "fields": {
                "from_currency": from_currency,
                "to_currency": to_currency,
                "exchange_rate": exchange_rate,
                "currency": currency,
                "created_at": timezone.now().isoformat()
            }
        }

    def split_currency_pair(currency_pair):
        return currency_pair[:3], currency_pair[3:]

    pk = 1
    for pair in REQUIRED_CURRENCY_PAIRS:
        data = yf.Ticker(f"{pair}=X").history_metadata

        exchange_rate_currency = data['currency']
        exchange_rate = float(data['regularMarketPrice'])

        # split the currencies
        first_currency, second_currency = split_currency_pair(pair)

        # Check if currency code already exists in the list before appending
        if not any(d['fields']['code'] == first_currency for d in currencies_model_data_list):
            currencies_model_data_list.append(create_currency_model_data(first_currency))
        if not any(d['fields']['code'] == second_currency for d in currencies_model_data_list):
            currencies_model_data_list.append(create_currency_model_data(second_currency))

        exchange_rates_model_data_list.append(create_exchange_rate_model_data(
            first_currency,
            second_currency,
            exchange_rate,
            exchange_rate_currency,
            pk
        ))

        pk += 1

    fixture_data = currencies_model_data_list + exchange_rates_model_data_list

    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, '../fixtures/fixture.json')

    with open(file_path, 'w') as f:
        json.dump(fixture_data, f)
        print("File created")
