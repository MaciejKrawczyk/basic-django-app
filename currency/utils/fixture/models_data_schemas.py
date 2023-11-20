from django.utils import timezone


def create_currency_model_data(code):
    return {
        "model": "currency.currency",
        "fields": {
            "code": code
        }
    }


def create_exchange_rate_history_model_data(pk, currency_pair, index, open, high, low, close):
    return {
        "model": "currency.exchangeratehistory",
        "pk": pk,
        "fields": {
            "currency_pair_history": currency_pair,
            "date": index,
            "open": open,
            "high": high,
            "low": low,
            "close": close
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
