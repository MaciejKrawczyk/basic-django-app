from django.apps import AppConfig

from currency.utils.create_fixture import create_fixture


class CurrencyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'currency'

    def ready(self):
        create_fixture()
