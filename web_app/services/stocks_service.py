# web_app/services/stocks_service.py

import requests
import json

import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="C3O5DCA87F30CPFY")

symbol = "AAPL" # todo:ask for user input
#symbol = input("Please choose a symbol like 'AAPL': ")
print("SYMBOL:", symbol)

requests_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"
print(requests_url)

response = requests.get(requests_url)
print(type(response))
print(response.status_code)
print(type(response.text))

parsed_response = json.loads(response.text)
print(type(parsed_response))

# breakpoint()

latest_close = parsed_response["Time Series (Daily)"]["2020-04-23"]["4. close"]
print("LATEST CLOSING PRICE:", latest_close)