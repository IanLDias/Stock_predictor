import requests

import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import pandas as pd
import config_var

table=pd.read_html(config_var.sp_500_url)
df = table[0]
stocks = dict(zip(df['Security'], df['Symbol']))

#Cryptocurrency coin name and symbol
requested_data = requests.get(config_var.crypto_coin_url)
data = requested_data.json()['data']['coins']
coins = {}
for coin in data:
    coins[coin['name']] = coin['symbol'] 