import streamlit as st
from stocks import Stock_viz, Stock_forecast
from crypto import Crypto

Pages = ["Stocks", "Cryptocurrency"]
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(Pages))

if selection == "Stocks":
    stock_class = Stock_viz()
    stock_class.stock_sidebar()
    stock_class.news_viz()
    stock_class.raw_data()
    symbol = stock_class.symbol
    stock_forecast = Stock_forecast(symbol)
    stock_forecast.forecast_viz()

if selection == "Cryptocurrency":
    crypto_class = Crypto()
    crypto_class.news_viz()
    crypto_class.crypto_summary()
    crypto_class.crypto_func()
    crypto_class.forecast_viz()

# country = st.sidebar.selectbox("Select country", ["Australia", "United States"])
# if country:
#     economic_term = st.sidebar.multiselect("Economic measures", ["Gross Domestic Product", 
#     "Interest Rate", "Unemployment Rate", "Retail sales performance"])

