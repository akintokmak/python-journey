import requests
import os
from dotenv import load_dotenv

load_dotenv()

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

stock_params = {
        "function":"TIME_SERIES_DAILY",
        "symbol":STOCK_NAME,
        "apikey":STOCK_API_KEY,
    }

response = requests.get(STOCK_ENDPOINT,params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list: list = [value for (key,value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "⬆️"
else:
    up_down = "⬇️"

diff_percent = round(difference / float(yesterday_closing_price) * 100)

if abs(diff_percent) > 1:
    news_params = {
        "apikey":NEWS_API_KEY,
        "qInTitle":COMPANY_NAME,
    }
    new_response = requests.get(NEWS_ENDPOINT,params=news_params)
    articles = new_response.json()["articles"]
    three_articles = articles[:3]

    formatted_article_list = [f"{STOCK_NAME} : {up_down} {diff_percent}% Headline: {article['title']}.\nBrief: {article['description']}" for article in three_articles]
    for article in formatted_article_list:
        telegram_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        telegram_params = {
            "chat_id": TELEGRAM_CHAT_ID,
            "text": article,
        }
        msg_response = requests.post(url=telegram_url, json=telegram_params)

        if msg_response.status_code == 200:
            print("Messages send successfully!")
        else:
            print("Error:", msg_response.text)
