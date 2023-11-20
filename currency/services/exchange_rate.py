from django.shortcuts import get_object_or_404

from currency.models import ExchangeRate


def get_exchange_rate(from_currency: str, to_currency: str):
    """
    Retrieve an exchange rate object based on from and to currencies
    """
    return get_object_or_404(ExchangeRate, from_currency=from_currency, to_currency=to_currency)
