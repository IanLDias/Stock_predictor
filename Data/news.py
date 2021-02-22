from config_var import today
import streamlit as st
import requests
@st.cache
def news(stock):
    url = (f'http://newsapi.org/v2/everything?q={stock}&from={today}$language=English&sortBy=popularity&apiKey=4507b4f67ba846e7b9a35228be9a69ae')

    response = requests.get(url)
    articles = response.json()['articles']
    return articles