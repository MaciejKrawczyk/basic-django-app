from django.apps import AppConfig

from currency.utils.FixtureCreator import FixtureCreator
from currency.utils.fixture.CurrencyModelDataCreator import CurrencyModelDataCreator
from currency.utils.fixture.ExchangeRateHistoryModelDataCreator import ExchangeRateHistoryModelDataCreator
from currency.utils.fixture.ExchangeRateModelDataCreator import ExchangeRateModelDataCreator
from currency.utils.utils import create_json_file


class CurrencyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'currency'

    def ready(self):

        currency_creator = CurrencyModelDataCreator()
        exchange_rate_creator = ExchangeRateModelDataCreator()
        history_creator = ExchangeRateHistoryModelDataCreator()

        fixture_creator = FixtureCreator(
            currency_creator=currency_creator,
            exchange_rate_creator=exchange_rate_creator,
            history_creator=history_creator
        )

        fixture_data = fixture_creator.create_fixture()

        create_json_file(fixture_data, '../fixtures/fixture.json')
