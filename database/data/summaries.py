import requests

import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import pandas as pd
import config_var

def get_information(name):
    name = name.replace(' ', '_')
    url = f'https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&titles={name}'
    information = requests.get(url)
    key = information.json()["query"]["pages"].keys()
    key = list(key)[0]
    return information.json()["query"]["pages"][key]['extract']
