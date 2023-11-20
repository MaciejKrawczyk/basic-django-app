import yfinance as yf

from currency.config import CURRENCY_RATE_HISTORY_PERIOD


def fetch_history_metadata_from_yf(pair: str):
    return yf.Ticker(f"{pair}=X").history_metadata


def fetch_history_from_yf(pair: str):
    return yf.Ticker(f"{pair}=X").history(period=CURRENCY_RATE_HISTORY_PERIOD)
