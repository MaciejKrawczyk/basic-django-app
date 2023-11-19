from django.shortcuts import get_object_or_404
from rest_framework import generics

from currency.models import Currency, ExchangeRate
from currency.serializers import CurrencySerializer, ExchangeRateSerializer


class CurrencyListAPIView(generics.ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class ExchangeRateDetailAPIView(generics.RetrieveAPIView):
    serializer_class = ExchangeRateSerializer

    def get_object(self):
        from_currency_code = self.kwargs['from_currency_code']
        to_currency_code = self.kwargs['to_currency_code']

        from_currency = get_object_or_404(Currency, code=from_currency_code)
        to_currency = get_object_or_404(Currency, code=to_currency_code)

        obj = get_object_or_404(ExchangeRate, from_currency=from_currency, to_currency=to_currency)
        self.check_object_permissions(self.request, obj)
        return obj
