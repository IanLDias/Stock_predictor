import streamlit as st

import streamlit as st

from database.data.raw_data import load_data, plot_raw_data_stock
from database.data.forecast import forecast
from database.data.news import news
from database.data.symbol_names import stocks, get_information
from config_var import today
from fbprophet.plot import plot_plotly

@st.cache
def data_load(symbol):
    return load_data(symbol)

class Stock_viz(object):
    'Provides the widgets and raw data for stocks'
    def __init__(self):
        self.symbol = None
        self.data = None
        self.stock_name = None
    def stock_sidebar(self):
        'Lots of widgets. Returns the stock_ticker (symbol) they select'
        self.stock_name = st.sidebar.selectbox("Select S&P500 company", list(stocks.keys()))
        self.symbol = stocks[self.stock_name]
        st.title(f"Stock Prediction for {self.stock_name}")
        st.header("Description")
        st.write(get_information(self.stock_name))
        return self.symbol, self.stock_name

    @st.cache
    def news_func(self):   
        print(self.stock_name)
        articles = news(self.stock_name)
        return articles

    def news_viz(self):
        if st.sidebar.checkbox('News'):
            articles = self.news_func()
            st.title(f"News for {self.stock_name}")
            for article in articles[:10]:
                st.subheader(article['title'])
                st.markdown(article['description'])

    #Loads the data associated with the stock
    @st.cache
    def _data_load(self):
        'Loads the data associated with the symbol. Called in self.raw_data'
        print("CACHE MISS DATA_LOAD")
        self.data = data_load(self.symbol)
        return self.data

    def raw_data(self):
        'Collects the raw data associated with the symbol'
        #data_load is an external function
        self.data = self._data_load()
        #Visualize the raw data
        if st.sidebar.checkbox('Raw data'):
            st.subheader('Raw data')
            st.dataframe(self.data.tail())
            fig = plot_raw_data_stock(self.data)
            st.plotly_chart(fig)


class Stock_forecast():
    def __init__(self, symbol):
        self.symbol = symbol
        self.n_years = None
        self.forecast = None
        self.m = None

    def forecast_viz(self):
        if st.sidebar.checkbox('Forecast'):
            self.n_years = st.slider("Years of prediction", 1, 4)
            data = data_load(self.symbol)
            self.m, self.forecast = forecast(self.n_years, data)
            st.subheader('Forecast data')
            st.write(self.forecast.tail())
            st.write('Forecast data')
            st.plotly_chart(self.forecast_graph())
            
    @st.cache(allow_output_mutation=True)
    def forecast_graph(self):
        return plot_plotly(self.m, self.forecast)

    @st.cache(allow_output_mutation=True)
    def forecast_components_graph(self, m, forecast):
        'NOT CURRENTLY ACCESSED'
        print("**COMPONENTS FIRST CACHE**")
        return m.plot_components(forecast)


    
#Plotting the raw data

#How far into the future to predict


