# importing the requests library
import requests
import random

# defining the api-endpoint
API_ENDPOINT = "http://127.0.0.1:8000/api/save-view/"

# data to be sent to api
data = {
  "instrument_id": 32344233,
  "trade_time_in_min": "2020-08-31T22:08",
  "open": random.randint(195,210),
  "high": random.randint(210,215),
  "low": random.randint(190,195),
  "close": random.randint(200,210),
  "indicator": "sma",
  "sample_rate": 12
}

# sending post request and saving response as response object
r = requests.post(url=API_ENDPOINT, data=data)

# extracting response text
pastebin_url = r.text
print("The pastebin URL is:%s" % pastebin_url)