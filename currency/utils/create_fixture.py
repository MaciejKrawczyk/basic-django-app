from django.utils import timezone
import yfinance as yf

REQUIRED_CURRENCY_PAIRS = ["EURUSD", "USDJPY", "PLNUSD"]


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


def fetch_data_from_yfinance(pair):
    return yf.Ticker(f"{pair}=X").history_metadata


def create_fixture(required_currency_pairs=REQUIRED_CURRENCY_PAIRS):
    currencies_model_data_list = []
    exchange_rates_model_data_list = []

    pk = 1
    for pair in required_currency_pairs:
        data = fetch_data_from_yfinance(pair)

        exchange_rate_currency = data['currency']
        exchange_rate = float(data['regularMarketPrice'])

        first_currency, second_currency = split_currency_pair(pair)

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

    return fixture_data
