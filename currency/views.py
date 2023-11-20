from django.shortcuts import get_object_or_404
from rest_framework import generics
from currency.models import Currency, ExchangeRate
from currency.serializers import CurrencySerializer, ExchangeRateSerializer


def get_currency(currency_code):
    """
    Retrieve a currency object based on its code
    """
    return get_object_or_404(Currency, code=currency_code)


def get_exchange_rate(from_currency, to_currency):
    """
    Retrieve an exchange rate object based on from and to currencies
    """
    return get_object_or_404(ExchangeRate, from_currency=from_currency, to_currency=to_currency)


class CurrencyListAPIView(generics.ListAPIView):
    """
    API view to list all currencies
    """
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class ExchangeRateDetailAPIView(generics.RetrieveAPIView):
    """
    API view to retrieve exchange rate details
    """
    serializer_class = ExchangeRateSerializer

    def get_object(self):
        """
        Retrieve the exchange rate object based on from and to currency codes
        """
        from_currency_code = self.kwargs['from_currency_code']
        to_currency_code = self.kwargs['to_currency_code']

        from_currency = get_currency(from_currency_code)
        to_currency = get_currency(to_currency_code)

        exchange_rate = get_exchange_rate(from_currency, to_currency)
        return exchange_rate
