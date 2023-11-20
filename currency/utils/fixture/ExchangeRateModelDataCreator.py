from django.utils import timezone

from currency.types import ModelDataCreator


class ExchangeRateModelDataCreator(ModelDataCreator):
    def create_model_data(self, exchange_rates_list, first_currency, second_currency, exchange_rate, currency, pk):
        return create_exchange_rate_model_data_list(exchange_rates_list, first_currency, second_currency, exchange_rate,
                                                    currency, pk)


# ---------------------------------------

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


def create_exchange_rate_model_data_list(exchange_rates_model_data_list, first_currency, second_currency, exchange_rate,
                                         exchange_rate_currency, pk):
    exchange_rates_model_data_list.append(create_exchange_rate_model_data(
        first_currency,
        second_currency,
        exchange_rate,
        exchange_rate_currency,
        pk
    ))
    return exchange_rates_model_data_list
