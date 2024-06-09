import json
import os
import requests
from lightweight_charts import Chart

symbol = '$NDX.X'

td_consumer_key = os.environ['TDKEY']
endpoint = 'https://api.tdameritrade.com/v1/marketdata/{stock_ticker}/quotes?'
full_url = endpoint.format(stock_ticker=symbol)
page = requests.get(url=full_url,
                    params={'apikey' : td_consumer_key})
content = json.loads(page.content)
print(content)

endpoint = 'https://api.tdameritrade.com/v1/marketdata/{stock_ticker}/pricehistory?periodType={periodType}&period={period}&frequencyType={frequencyType}&frequency={frequency}'
full_url = endpoint.format(stock_ticker=symbol,periodType='year',period=1,frequencyType='daily',frequency=1)
page = requests.get(url=full_url,
                    params={'apikey' : td_consumer_key})
content = json.loads(page.content)
print(content)