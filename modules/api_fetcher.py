import requests
import pandas as pd

import os
import requests

API_KEY = "give your own api key"  # Replace with your actual API key



def fetch_live_aqi(city, state, country):
    url = "https://api.airvisual.com/v2/city"
    params = {
        "city": city,
        "state": state,
        "country": country,
        "key": API_KEY
    }
    response = requests.get(url, params=params)

    if response.status_code != 200:
        raise Exception(f"API Error: {response.status_code} - {response.text}")

    data = response.json()
    if data.get("status") != "success":
        raise Exception(f"API returned error: {data.get('data')}")

    current_data = data["data"]["current"]["pollution"]

    pollutants = {
        "PM2.5": current_data.get("aqius", 0),
        "PM10": 0, "NO": 0, "NO2": 0, "NOx": 0, "NH3": 0,
        "CO": 0, "SO2": 0, "O3": 0, "Benzene": 0, "Toluene": 0, "Xylene": 0,
        "AQI": current_data.get("aqius", 0),
        "City": city,
        "Date": pd.Timestamp.now()
    }

    df = pd.DataFrame([pollutants])
    return df
