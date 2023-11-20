from django.test import TestCase
from currency.utils.FixtureCreator import FixtureCreator
from django.core.management import call_command
from currency.models import Currency, ExchangeRate, ExchangeRateHistory
from currency.utils.fixture.CurrencyModelDataCreator import CurrencyModelDataCreator
from currency.utils.fixture.ExchangeRateHistoryModelDataCreator import ExchangeRateHistoryModelDataCreator
from currency.utils.fixture.ExchangeRateModelDataCreator import ExchangeRateModelDataCreator


class CreateFixtureTest(TestCase):
    def setUp(self):
        self.currency_creator = CurrencyModelDataCreator()
        self.exchange_rate_creator = ExchangeRateModelDataCreator()
        self.history_creator = ExchangeRateHistoryModelDataCreator()

        self.fixture_creator = FixtureCreator(
            currency_creator=self.currency_creator,
            exchange_rate_creator=self.exchange_rate_creator,
            history_creator=self.history_creator
        )

    def test_create_fixture(self):
        fixture_data = self.fixture_creator.create_fixture()

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
