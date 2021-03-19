import requests
import pandas as pd
import json

class GetData:
    def BinanceData(self):
        empty_str = ''
        url = "https://api.binance.com/api/v1/ticker/24hr"
        data = requests.get(url).json()
        empty_str.append(data)                     
        for dat in data:
            data.append(empty_str)
        with open('data.json','a') as dataimport:
            dataimport.write(empty_str)
            dataimport.close()



g = GetData()
g.BinanceData()