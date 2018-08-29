from datetime import datetime, timedelta

import requests

url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

def coins_data():
    payload = dict()
    payload["X-CMC_PRO_API_KEY"] = "" // key
    response = requests.get(url, headers = payload)
    return response.ok, response.json()
