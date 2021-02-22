import streamlit as st

    
from Data.raw_data import load_data, plot_raw_data
from Data.forecast import forecast
from Data.news import news
from config_var import today
from Data.symbol_names import stocks, get_information
from fbprophet.plot import plot_plotly

#Drop down menu of stocks (ticker form)
stock_name = st.sidebar.selectbox("Select dataset for prediction", list(stocks.keys()))
stock_ticker = stocks[stock_name]


st.title(f"Stock Prediction for {stock_name}")

st.write(get_information(stock_name))
#analysis = ["Raw Data", "Forecast Data", "News"]
#selected_analysis = st.selectbox("Analysis", analysis)

#Loads the data associated with the stock
data = load_data(stock_ticker)

#Plotting the raw data
def raw_data():
    st.subheader('Raw data')
    st.write(data.tail())

    fig = plot_raw_data(data)
    st.plotly_chart(fig)

#How far into the future to predict
raw_data()
n_years = st.slider("Years of prediction", 1, 4)

#Uses Prophet to predict
m, forecast = forecast(n_years, data)

#Plots the forecast
st.subheader('Forecast data')
st.write(forecast.tail())

st.write('Forecast data')
forecast_fig = plot_plotly(m, forecast)
st.plotly_chart(forecast_fig)

st.write('Forecast components')
components_fig = m.plot_components(forecast)
st.write(components_fig)

st.title(f"News for {stock_name}")   
articles = news(stock_name)
for article in articles[:10]:
    st.subheader(article['title'])
    st.markdown(article['description'])

#Table of the relevant news associated with the stock