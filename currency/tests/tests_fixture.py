from django.test import TestCase
from currency.utils.create_fixture import create_fixture
from django.core.management import call_command
from currency.models import Currency, ExchangeRate


class CreateFixtureTest(TestCase):
    def test_create_fixture(self):
        fixture_data = create_fixture()

        # Assert that the returned value is a list
        self.assertIsInstance(fixture_data, list)

        # Assert that the list is not empty
        self.assertTrue(fixture_data)

        for data in fixture_data:
            # Assert that each item in the list is a dictionary with the keys "model" and "fields"
            self.assertIn('model', data)
            self.assertIn('fields', data)

            # For the "fields" key, assert that it contains the necessary keys based on the "model" key
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
        # Load the fixture
        call_command('loaddata', 'fixture.json')

    def test_fixture_loaded(self):
        # Check if the data from the fixture is present in the database
        self.assertTrue(Currency.objects.exists())
        self.assertTrue(ExchangeRate.objects.exists())
