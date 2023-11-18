from django.apps import AppConfig
import yfinance as yf


REQUIRED_CURRENCY_PAIRS = ["EURUSD", "USDJPY", "PLNUSD"]


class CurrencyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'currency'

    def ready(self):

        from .models import Currency, ExchangeRate

        def split_currency_pair(currency_pair):
            return currency_pair[:3], currency_pair[3:]

        for pair in REQUIRED_CURRENCY_PAIRS:
            data = yf.Ticker(f"{pair}=X").history_metadata

            exchange_rate_currency = data['currency']
            exchange_rate = float(data['regularMarketPrice'])

            # split the currencies
            first_currency, second_currency = split_currency_pair(pair)

            first_currency_obj, is_created1 = Currency.objects.get_or_create(
                code=first_currency
            )
            second_currency_obj, is_created2 = Currency.objects.get_or_create(
                code=second_currency
            )

            if ExchangeRate.objects.filter(from_currency=first_currency_obj, to_currency=second_currency_obj).exists():
                print("exist")
            else:
                exchange_rate_obj, is_created3 = ExchangeRate.objects.get_or_create(
                    from_currency=first_currency_obj,
                    to_currency=second_currency_obj,
                    exchange_rate=exchange_rate,
                    currency=exchange_rate_currency
                )
