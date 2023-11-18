from django.db import models


class Currency(models.Model):
    code = models.CharField(max_length=3, primary_key=True)


# I created the second table for currency exchanges for better scalability and performance.
class ExchangeRate(models.Model):
    from_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='from_currency')
    to_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='to_currency')
    exchange_rate = models.DecimalField(max_digits=15, decimal_places=2, default=00.00)
    created_at = models.DateTimeField(auto_now_add=True)
    currency = models.CharField(max_length=3, default='USD')

    @property
    def currency_pair(self):
        return f'{self.from_currency.code}{self.to_currency.code}'
