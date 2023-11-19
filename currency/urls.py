from django.urls import path
from . import views
from .admin import historical_rates

urlpatterns = [
    path('new-url/<int:id>/', historical_rates, name='historical_rates'),
    path('', views.CurrencyListAPIView.as_view(), ),
    path('<str:from_currency_code>/<str:to_currency_code>/', views.ExchangeRateDetailAPIView.as_view(), ),
]