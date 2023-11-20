def create_currency_model_data(code):
    return {
        "model": "currency.currency",
        "fields": {
            "code": code
        }
    }


def create_currency_model_data_list(currencies_model_data_list, first_currency, second_currency):
    if not any(d['fields']['code'] == first_currency for d in currencies_model_data_list):
        currencies_model_data_list.append(create_currency_model_data(first_currency))
    if not any(d['fields']['code'] == second_currency for d in currencies_model_data_list):
        currencies_model_data_list.append(create_currency_model_data(second_currency))
    return currencies_model_data_list
