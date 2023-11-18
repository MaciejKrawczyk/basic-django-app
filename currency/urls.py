from django.urls import path
from . import views

urlpatterns = [
    path('', views.CurrencyListAPIView.as_view(), ),
    path('<str:from_currency_code>/<str:to_currency_code>/', views.ExchangeRateDetailAPIView.as_view(), ),
]