import requests
import json

def prod_exchange():
    api_call = requests.get('http://api.exchangeratesapi.io/v1/latest?access_key=36d4d7b23910dc84442f4bc147637fab').json()  # no spaces, http and not https
    get_rates = api_call['rates']
    currency_list = list(k for k, v in get_rates.items() if v < 10)
    return json.dumps(currency_list, indent=4)

print (prod_exchange())

def dev_exchange():
    parsed = json.load(open('all_currency_file_new.json', "r"))
    get_rates = parsed["rates"]
    currency_list = list(k for k, v in get_rates.items() if v < 10)
    return json.dumps(currency_list, indent=4)

print(dev_exchange())

# i've used the text below one time to create json file with all the currency in the api
'''

def dev_exchange():
    currency_names = []
    api_call = requests.get('http://api.exchangeratesapi.io/v1/latest?access_key=36d4d7b23910dc84442f4bc147637fab').json()
    with open('all_currency_file_new.json', 'w') as outfile:
        json.dump(api_call, outfile, indent=4)

dev_exchange()

'''