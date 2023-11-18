
from django.test import TestCase

from currency.models import Currency, ExchangeRate


class CurrencyModelTest(TestCase):
    def test_currency_creation(self):
        Currency.objects.create(code='USD')
        self.assertEqual(Currency.objects.count(), 1)


class ExchangeRateModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.currency1 = Currency.objects.create(code='USD')
        cls.currency2 = Currency.objects.create(code='EUR')

    def test_exchange_rate_creation(self):
        ExchangeRate.objects.create(from_currency=self.currency1, to_currency=self.currency2)
        self.assertEqual(ExchangeRate.objects.count(), 1)


class CurrencyListViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/currency/')
        self.assertEqual(response.status_code, 200)


class ExchangeRateDetailViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.currency1 = Currency.objects.create(code='USD')
        cls.currency2 = Currency.objects.create(code='EUR')
        ExchangeRate.objects.create(from_currency=cls.currency1, to_currency=cls.currency2)

    def test_valid_exchange_rate_request(self):
        response = self.client.get('/currency/USD/EUR/')
        self.assertEqual(response.status_code, 200)

