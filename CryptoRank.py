import requests
import json
import datetime as dt  

#GLOBAL VARIABLES
count = 1

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '046bcd29-c2fc-4482-8368-a05d8df8efdd'
}

params = {
    'start': '1',
    'limit': '20',
    'convert': 'USD'
}

url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
json_data = requests.get(url, params=params, headers=headers).json()

crypto_coins = json_data['data']

# UI
print("****Welcome To My Latest Crpto Rank Inspector****")
print("Credit: Ahmet Kırmızı")
print("Github: ahmetk5113")
print()
print()

# LOGIC
for c in crypto_coins:
    CoinSym = c['symbol']
    CoinName = c['name']
    Cprice = c['quote']['USD']['price']
    Csupply = c['circulating_supply']
    ClastUpdate = c['last_updated']
    Pchangehour = c['quote']['USD']['percent_change_1h']
    print(f"Symbol for rank {count} Crypto is:")
    print(CoinSym)
    count = count + 1