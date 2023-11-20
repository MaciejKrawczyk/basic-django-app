from django.db import models


class Currency(models.Model):
    code = models.CharField(max_length=3, primary_key=True)

    class Meta:
        app_label = 'currency'
        ordering = ['code']
        verbose_name = 'Currency'
        verbose_name_plural = 'Currencies'

    def __str__(self):
        return self.code
