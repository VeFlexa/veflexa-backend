import requests
import datetime

def fetch_prices():
    today = datetime.date.today()
    url = f"https://api.esios.ree.es/indicators/1001?start_date={today}&end_date={today}"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data
