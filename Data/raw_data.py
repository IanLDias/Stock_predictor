import streamlit as st
import yfinance as yf
from config import start_date, today
from plotly import graph_objects as go

@st.cache
def load_data(ticker):
    data = yf.download(ticker, start_date, today)
    data.reset_index(inplace=True)
    return data

def plot_raw_data(data):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name='stock_open'))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name='stock_close'))
    fig.layout.update(title_text = "Time Series Data", xaxis_rangeslider_visible=True)
    return fig

