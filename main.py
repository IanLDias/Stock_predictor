import streamlit as st

from Data.raw_data import load_data, plot_raw_data
from Data.forecast import forecast
from Data.news import news
from Data.symbol_names import stocks, get_information

from config_var import today

from fbprophet.plot import plot_plotly


#Drop down menu of stocks (ticker form)
stock_name = st.sidebar.selectbox("Select dataset for prediction", list(stocks.keys()))
stock_ticker = stocks[stock_name]


st.title(f"Stock Prediction for {stock_name}")

st.header("Description")
st.write(get_information(stock_name))


#Loads the data associated with the stock
@st.cache
def data_load(stock_ticker):
    print("CACHE MISS DATA_LOAD")
    return load_data(stock_ticker)

data = data_load(stock_ticker)

@st.cache
def forecast_func(n_years, data):
    print('FIRST CACHE OF FORECAST')
    return forecast(n_years, data)

@st.cache(allow_output_mutation=True)
def forecast_graph(m, forecast):

    return plot_plotly(m, forecast)

@st.cache(allow_output_mutation=True)
def forecast_components_graph(forecast_local):
    print("**COMPONENTS FIRST CACHE**")
    return m.plot_components(forecast_local)

@st.cache
def news_func():   
    articles = news(stock_name)
    return articles
    
#Plotting the raw data

#How far into the future to predict

if st.sidebar.checkbox('Raw data'):
    st.subheader('Raw data')
    st.dataframe(data.tail())
    fig = plot_raw_data(data)
    st.plotly_chart(fig)

if st.sidebar.checkbox('Forecast'):
    n_years = st.slider("Years of prediction", 1, 4)
    m, forecast = forecast_func(n_years, data)

    st.subheader('Forecast data')
    #Changed to local to be able to implement caching for forecast_graph
    st.write(forecast.tail())
    st.write('Forecast data')
    st.plotly_chart(forecast_graph(m, forecast))

    st.write('Forecast components')
    st.write(forecast_components_graph(forecast))

if st.sidebar.checkbox('News'):
    articles = news_func()
    st.title(f"News for {stock_name}")
    for article in articles[:10]:
        st.subheader(article['title'])
        st.markdown(article['description'])
