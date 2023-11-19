from django.test import TestCase

from currency.models import Currency


class CurrencyModelTest(TestCase):
    def test_currency_creation(self):
        Currency.objects.create(code='USD')
        self.assertEqual(Currency.objects.count(), 1)


class CurrencyListViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/currency/')
        self.assertEqual(response.status_code, 200)
