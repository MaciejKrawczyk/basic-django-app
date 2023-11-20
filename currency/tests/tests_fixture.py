from django.test import TestCase
from currency.utils.FixtureCreator import create_fixture
from django.core.management import call_command
from currency.models import Currency, ExchangeRate, ExchangeRateHistory


class CreateFixtureTest(TestCase):
    def test_create_fixture(self):
        fixture_data = create_fixture()

        self.assertIsInstance(fixture_data, list)

        self.assertTrue(fixture_data)

        for data in fixture_data:

            self.assertIn('model', data)
            self.assertIn('fields', data)

            if data['model'] == 'currency.currency':
                self.assertIn('code', data['fields'])
            elif data['model'] == 'currency.exchangerate':
                self.assertIn('from_currency', data['fields'])
                self.assertIn('to_currency', data['fields'])
                self.assertIn('exchange_rate', data['fields'])
                self.assertIn('currency', data['fields'])
                self.assertIn('created_at', data['fields'])


class LoadFixtureTest(TestCase):
    def setUp(self):
        call_command('loaddata', 'fixture.json')

    def test_fixture_loaded(self):
        self.assertTrue(Currency.objects.exists())
        self.assertTrue(ExchangeRate.objects.exists())
        self.assertTrue(ExchangeRateHistory.objects.exists())

