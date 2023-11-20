from currency.utils.utils import split_currency_pair
import yfinance as yf

REQUIRED_CURRENCY_PAIRS = ["EURUSD", "USDJPY", "PLNUSD"]
CURRENCY_RATE_HISTORY_PERIOD = "1mo"


def fetch_history_metadata_from_yf(pair: str):
    return yf.Ticker(f"{pair}=X").history_metadata


def fetch_history_from_yf(pair: str):
    return yf.Ticker(f"{pair}=X").history(period=CURRENCY_RATE_HISTORY_PERIOD)


class FixtureCreator:
    def __init__(self, currency_creator=None, exchange_rate_creator=None, history_creator=None):
        self.currency_creator = currency_creator
        self.exchange_rate_creator = exchange_rate_creator
        self.history_creator = history_creator

    def create_fixture(self, required_currency_pairs=REQUIRED_CURRENCY_PAIRS):
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

            if self.currency_creator:
                currencies_model_data_list = self.currency_creator.create_model_data(
                    currencies_model_data_list, first_currency, second_currency)

            if self.exchange_rate_creator:
                exchange_rates_model_data_list = self.exchange_rate_creator.create_model_data(
                    exchange_rates_model_data_list, first_currency, second_currency, exchange_rate, exchange_rate_currency, pk)

            if self.history_creator:
                history_data = fetch_history_from_yf(pair)
                exchange_rates_history_model_data_list, exchange_rate_history_pk = self.history_creator.create_model_data(
                    exchange_rates_history_model_data_list, exchange_rate_history_pk, pk, history_data)

            pk += 1

        fixture_data = []
        if self.currency_creator:
            fixture_data.extend(currencies_model_data_list)
        if self.exchange_rate_creator:
            fixture_data.extend(exchange_rates_model_data_list)
        if self.history_creator:
            fixture_data.extend(exchange_rates_history_model_data_list)

        return fixture_data


