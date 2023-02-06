from requests import Session
import json
from prettytable import PrettyTable

#top-10 coin api-endpoint
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
parameters = {
       'sort' : 'cmc_rank',
       'limit': '10',
       }
headers = {
       'Accepts': 'application/json',
       'X-CMC_PRO_API_KEY': '________ YOUR API KEY __________'
       }

session = Session()
session.headers.update(headers)
response =session.get(url, params=parameters)
json_response=(json.loads(response.text))


symbol_list = [coin['symbol'] for coin in json_response['data'] ]

""" symbol_list = []
for coin in json_response['data']:
       item=(coin['symbol'])
       symbol_list.append(item) """

#latest price loop      
coin_price = []
for i in range(10):
              
              url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

              headers = {
              'Accepts': 'application/json',
              'X-CMC_PRO_API_KEY': '________ YOUR API KEY __________'
              }
              parameters = {
              'symbol' : symbol_list[i],
              'convert' : 'USD'
              }

              session = Session()
              session.headers.update(headers)
              response =session.get(url, params=parameters)

              raw_price = float(json.loads(response.text)['data'][f'{symbol_list[i]}']['quote']['USD']['price'])
              round_price = round(raw_price,3)
              
              coin_price.append(round_price)

pretty = PrettyTable()
pretty.add_column("Coin",symbol_list)
pretty.add_column("Price",coin_price)
print(pretty)

      
