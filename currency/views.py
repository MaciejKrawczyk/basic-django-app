from rest_framework import generics
from currency.models import Currency
from currency.serializers import CurrencySerializer, ExchangeRateSerializer
from currency.services.currency import get_currency
from currency.services.exchange_rate import get_exchange_rate


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
