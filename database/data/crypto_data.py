url = f"https://api.coinranking.com/v2/coins"
import requests
from datetime import datetime
import pandas as pd
from plotly import graph_objects as go

requested_data = requests.get(url)

data = requested_data.json()['data']['coins']


coins = {}
for coin in data:
    coins[coin['name']] = coin['symbol'] 

API_KEY_COMP = '17666b6cf3df20d3d971212b0646e2a15447b36bf7b7a4974283778402417772'
BASE_URL_COMP = 'https://min-api.cryptocompare.com/'

def convert_unix_to_datetime(date_col):
    'Converts the unix dates into YYYY-MM-DD'
    int_list = list((map(int,date_col)))
    date_list = list(map(datetime.utcfromtimestamp, int_list))
    converted_dates = [date_list[i].strftime('%Y-%m-%d') for i in range(len(date_list))]
    return converted_dates

def crypto_gather_data(name):
    symbol = coins[name]
    url = f'{BASE_URL_COMP}data/v2/histoday?fsym={symbol}&tsym=USD&limit=2000&api_key={API_KEY_COMP}'
    requested_data = requests.get(url)
    data = requested_data.json()
    data = data['Data']['Data']
    df = pd.DataFrame(data)
    df['time'] = convert_unix_to_datetime(df['time'])
    return df

print(crypto_gather_data('Bitcoin'))

def plot_raw_data_crypto(data):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['time'], y=data['open'], name='open'))
    fig.add_trace(go.Scatter(x=data['time'], y=data['close'], name='close'))
    fig.layout.update(title_text = "Time Series Data", xaxis_rangeslider_visible=True)
    return fig

