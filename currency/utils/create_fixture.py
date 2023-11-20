import yfinance as yf
from currency.utils.fixture.models_data_schemas import create_currency_model_data, create_exchange_rate_model_data, \
    create_exchange_rate_history_model_data

REQUIRED_CURRENCY_PAIRS = ["EURUSD", "USDJPY", "PLNUSD"]
CURRENCY_RATE_HISTORY_PERIOD = "1mo"


def split_currency_pair(currency_pair):
    return currency_pair[:3], currency_pair[3:]


def fetch_history_metadata_from_yf(pair):
    return yf.Ticker(f"{pair}=X").history_metadata


def fetch_history_from_yf(pair):
    return yf.Ticker(f"{pair}=X").history(period=CURRENCY_RATE_HISTORY_PERIOD)


def create_fixture(required_currency_pairs=REQUIRED_CURRENCY_PAIRS):
    currencies_model_data_list = []
    exchange_rates_model_data_list = []
    exchange_rates_history_model_data_list = []

    pk = 1
    exchange_rate_history_pk = 1
    for pair in required_currency_pairs:
        history_metadata = fetch_history_metadata_from_yf(pair)

        exchange_rate_currency = history_metadata['currency']
        exchange_rate = float(history_metadata['regularMarketPrice'])

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

        history_data = fetch_history_from_yf(pair)
        for index, row in history_data.iterrows():
            exchange_rates_history_model_data_list.append(create_exchange_rate_history_model_data(
                exchange_rate_history_pk,
                pk,
                index.strftime('%Y-%m-%d'),
                row['Open'],
                row['High'],
                row['Low'],
                row['Close']
            ))
            exchange_rate_history_pk += 1

        pk += 1

    fixture_data = currencies_model_data_list + exchange_rates_model_data_list + exchange_rates_history_model_data_list

    return fixture_data
