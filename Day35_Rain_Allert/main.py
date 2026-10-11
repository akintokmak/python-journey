import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get("OWM_API_KEY")
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")


MY_LAT = 39.480245
MY_LON = 29.900808

weather_params = {
    "lat" : MY_LAT,
    "lon" : MY_LON,
    "appid" : api_key,
    "cnt": 4,
}

response = requests.get(url=OWM_Endpoint, params=weather_params)
response.raise_for_status()

weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    telegram_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    telegram_params = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": "It's going to rain today. Remember to bring an umbrella!  ☔"
    }

    msg_response = requests.post(url=telegram_url, json=telegram_params)

    if msg_response.status_code == 200:
        print("Messages send successfully!")
    else:
        print("Error:", msg_response.text)
