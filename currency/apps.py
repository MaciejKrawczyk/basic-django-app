from django.apps import AppConfig

from currency.utils.create_fixture import create_fixture
from currency.utils.utils import create_json_file


class CurrencyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'currency'

    def ready(self):
        fixture_data = create_fixture()
        create_json_file(fixture_data, '../fixtures/fixture.json')
