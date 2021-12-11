import requests
import json


def prod_exchange():
    currency_names = []
    api_call = requests.get('http://api.exchangeratesapi.io/v1/latest?access_key=36d4d7b23910dc84442f4bc147637fab').json()  # no spaces, http and not https
    get_rates = api_call['rates']
    for k, v in get_rates.items():
        if v < 10:
            currency_names.append(k)
    return json.dumps(currency_names, indent=4)


print (prod_exchange())

def dev_exchange():
    print('dev')
    currency_names = []
    parsed = json.load(open('all_currency_file_new.json', "r"))
    get_rates = parsed["rates"]
    for k, v in get_rates.items():
        if v < 10:
            currency_names.append(k)
    return json.dumps(currency_names, indent=4)



print(dev_exchange())


#i've used the text below one time to create json file with all of the currency in the api

'''

def dev_exchange():
    currency_names = []
    api_call = requests.get('http://api.exchangeratesapi.io/v1/latest?access_key=36d4d7b23910dc84442f4bc147637fab').json()
    get_rates = api_call["rates"]
    for k, v in get_rates.items():
        currency_names.append(k)

    with open('all_currency_file_new.json', 'w') as outfile:
        json.dump(api_call, outfile)

dev_exchange()

'''
