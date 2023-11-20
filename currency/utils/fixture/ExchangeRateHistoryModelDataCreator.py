from currency.types import ModelDataCreator


class ExchangeRateHistoryModelDataCreator(ModelDataCreator):
    def create_model_data(self, history_list, history_pk, pk, history_data):
        return create_exchange_rate_history_model_data_list(history_list, history_pk, pk, history_data)


# --------------------------------------

def create_exchange_rate_history_model_data(pk, currency_pair, index, open, high, low, close):
    return {
        "model": "currency.exchangeratehistory",
        "pk": pk,
        "fields": {
            "currency_pair_history": currency_pair,
            "date": index,
            "open": open,
            "high": high,
            "low": low,
            "close": close
        }
    }


def create_exchange_rate_history_model_data_list(exchange_rates_history_model_data_list, exchange_rate_history_pk, pk,
                                                 history_data):
    for index, row in history_data.iterrows():
        exchange_rates_history_model_data_list.append(create_exchange_rate_history_model_data(
            exchange_rate_history_pk,
            pk,
            index.strftime('%Y-%m-%d'),
            row['Open'],
            row['High'],
            row['Low'],
            row['Close']
        ))
        exchange_rate_history_pk += 1
    return exchange_rates_history_model_data_list, exchange_rate_history_pk
