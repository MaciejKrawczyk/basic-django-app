from rest_framework import serializers

from currency.models import ExchangeRate


class ExchangeRateSerializer(serializers.ModelSerializer):
    currency_pair = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = ExchangeRate
        fields = [
            "currency_pair",
            "exchange_rate"
        ]

    def get_currency_pair(self, obj):
        return obj.currency_pair
