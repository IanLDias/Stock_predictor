import config_var
import streamlit as st
import requests

@st.cache
def news(stock):
    url = config_var.stock_news_url(stock)
    response = requests.get(url)
    articles = response.json()['articles']
    return articles

