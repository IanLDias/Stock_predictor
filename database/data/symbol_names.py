import requests

import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import pandas as pd

table=pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
df = table[0]
df.to_csv('S&P500-Info.csv')
df.to_csv("S&P500-Symbols.csv", columns=['Symbol'])
stocks = dict(zip(df['Security'], df['Symbol']))

def get_information(name):
    name = name.replace(' ', '_')
    url = f'https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&titles={name}'
    information = requests.get(url)
    key = information.json()["query"]["pages"].keys()
    key = list(key)[0]
    return information.json()["query"]["pages"][key]['extract']
