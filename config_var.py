from datetime import date
import requests


#gets list of all crypto coins
crypto_coin_url = "https://api.coinranking.com/v2/coins"

#gets time series information of crypto coins
API_KEY_COMP = '17666b6cf3df20d3d971212b0646e2a15447b36bf7b7a4974283778402417772'
BASE_URL_COMP = 'https://min-api.cryptocompare.com/'

#list of all s&p500 by name
sp_500_url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
start_date = "2014-01-01"
today = date.today().strftime("%Y-%m-%d")

#News of individual stocks
stock_news_api_key = '4507b4f67ba846e7b9a35228be9a69ae'
def stock_news_url(stock):
    return f'http://newsapi.org/v2/everything?q={stock}&from={today}$language=English&sortBy=popularity&apiKey={stock_news_api_key}'

#Steps to update:
#1) Save code to github
#2) Connect to EC2 instance
#    ssh -i "streamlit_app.pem" ubuntu@ec2-####.us-east-2.compute.amazonaws.com
#3) Remove current remove (rm -rf <name>), git clone new repo
#4) Delete/update docker on the VM
#5) docker image build -t streamlit:app .
#   Delete current container
#       docker container ls -a
#       docker container stop <container id?
#       docker container rm <container id> 
#6) docker container run -p 8501:8501 -d streamlit:app

