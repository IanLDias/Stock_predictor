import streamlit as st
from database.data.crypto_data import coins
from database.data.crypto_data import crypto_gather_data
from database.data.crypto_data import plot_raw_data_crypto

def crpyto_func():
    crypto_name = st.sidebar.selectbox("Select cryptocurrency", list(coins.keys()))
    if st.sidebar.checkbox('Raw data', key=1):
        data = crypto_gather_data(crypto_name)
        st.subheader('Raw data')
        st.dataframe(data.tail())
        fig = plot_raw_data_crypto(data)
        st.plotly_chart(fig)
        
    st.sidebar.checkbox('Forecast', key=1)
    st.sidebar.checkbox('News', key=1)