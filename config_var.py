from datetime import date
import requests

api_key = '4507b4f67ba846e7b9a35228be9a69ae'

#stocks = {"AAPL": "Apple", "GOOG": "Google", "MSFT": "Microsoft", "GME": "Gamestop"}
start_date = "2014-01-01"
today = date.today().strftime("%Y-%m-%d")

#command to rebuild:
#az acr build --registry StockPredictorRegistry --resource-group StockPredictor --image main .

#az webapp config appsettings set --resource-group StockPredictor --name stock-predictor-web-app --settings WEBSITES_PORT=80



# WEBSITES_CONTAINER_START_TIME_LIMIT=1800
# disableWatchdogWarning = false
# sharingMode = “off”
# showWarningOnDirectExecution = true
# logLevel = “debug”
# caching = true
# displayEnabled = true
# magicEnabled = true
# fixMatplotlib = true
# port = 80
# serverPort = 80