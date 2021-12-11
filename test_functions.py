import pytest
import main
import json
import requests


@pytest.mark.prod_exchange
def test_prod_exchange():
    currency_list = []
    response = requests.get('http://api.exchangeratesapi.io/v1/latest?access_key=36d4d7b23910dc84442f4bc147637fab').json()
    get_rates = response["rates"]
    for k, v in get_rates.items():
        if v >= 10:
            currency_list.append(k)
    nice_formatted_currency_list = json.dumps(currency_list, indent=4)
    list_from_main = main.prod_exchange()
    assert nice_formatted_currency_list not in list_from_main



@pytest.mark.dev_exchange
def test_dev_exchange():
    currency_list = []
    response = json.load(open('all_currency_file_new.json', 'r'))
    get_rates = response["rates"]
    for k, v in get_rates.items():
        if v >= 10:
            currency_list.append(k)
    nice_formatted_currency_list = json.dumps(currency_list,indent=4)
    list_from_main = main.dev_exchange()
    assert nice_formatted_currency_list not in list_from_main