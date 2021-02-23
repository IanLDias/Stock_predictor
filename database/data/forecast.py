from fbprophet import Prophet
from fbprophet.plot import plot_plotly

def forecast(n_years, data):
    period = n_years * 365

    df_train = data[['Date', 'Close']]
    df_train = df_train.rename(columns={'Date': 'ds', 'Close': 'y'})

    m = Prophet()
    m.fit(df_train)
    future = m.make_future_dataframe(periods=period)
    forecast = m.predict(future)
    return m, forecast

def forecast_crypto(n_months, data):
    period = n_months * 30
    df_train = data[['time', 'close']]
    df_train = df_train.rename(columns={'time': 'ds', 'close': 'y'})
    
    m = Prophet()
    m.fit(df_train)
    future = m.make_future_dataframe(periods=period)
    forecast = m.predict(future)
    return m, forecast