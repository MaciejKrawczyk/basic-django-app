from django.db import models

from currency.models import ExchangeRate


class ExchangeRateHistory(models.Model):
    currency_pair_history = models.ForeignKey(ExchangeRate, on_delete=models.CASCADE, related_name='currency_pair_history')
    date = models.DateField()
    open = models.DecimalField(max_digits=15, decimal_places=7, default=00.00)
    high = models.DecimalField(max_digits=15, decimal_places=7, default=00.00)
    low = models.DecimalField(max_digits=15, decimal_places=7, default=00.00)
    close = models.DecimalField(max_digits=15, decimal_places=7, default=00.00)

    class Meta:
        app_label = 'currency'
        verbose_name = 'Exchange Rate History'
        verbose_name_plural = 'Exchange Rates History'
