import streamlit as st
from database.data.crypto_data import coins
from database.data.crypto_data import crypto_gather_data
from database.data.crypto_data import plot_raw_data_crypto
from database.data.forecast import forecast_crypto
from database.data.summaries import get_information
from database.data.news import news

from fbprophet.plot import plot_plotly

class Crypto:
    def __init__(self):
        self.crypto_name = st.sidebar.selectbox("Select Cryptocurrency", list(coins.keys()))
        self.news_display = st.sidebar.checkbox('News', key=1)
        self.raw_data = st.sidebar.checkbox('Raw data', key=1)
        self.forecast = st.sidebar.checkbox('Forecast', key=1)

    @st.cache
    def news_func(self):   
        if self.news_display:
            articles = news(self.crypto_name)
            return articles

    def news_viz(self):
        if self.news_display:
            articles = self.news_func()
            st.title(f"News for {self.crypto_name}")
            for article in articles[:10]:
                st.subheader(article['title'])
                st.markdown(article['description'])
    @st.cache
    def _data_load(self):
        data = crypto_gather_data(self.crypto_name)
        return data

    def crypto_summary(self):
        if self.crypto_name:
            st.title(f"Overview for {self.crypto_name}")
            st.header("Description")
            st.write(get_information(self.crypto_name))

    def crypto_func(self):
        if self.raw_data:
            data = self._data_load()
            st.subheader('Raw data')
            st.dataframe(data.tail())
            fig = plot_raw_data_crypto(data)
            st.plotly_chart(fig)

    def forecast_viz(self):
        if self.forecast:
            data = self._data_load()
            self.n_months = st.slider("Months of prediction", 1, 12)
            self.m, self.forecast = forecast_crypto(self.n_months, data)
            st.subheader('Forecast data')
            st.write(self.forecast.tail())
            st.write('Forecast data')
            st.plotly_chart(self.forecast_graph())
            
    @st.cache(allow_output_mutation=True)
    def forecast_graph(self):
        return plot_plotly(self.m, self.forecast)

