from django.shortcuts import get_object_or_404
from currency.models import Currency


def get_currency(currency_code: str):
    """
    Retrieve a currency object based on its code
    """
    return get_object_or_404(Currency, code=currency_code)
