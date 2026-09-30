import time

import requests
from datetime import datetime
import smtplib
import os

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

MY_LAT = 39.479867
MY_LONG = 29.915400

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 8,
    }

    response = requests.get(url="https://api.sunrise-sunset.org/v2", params=parameters)
    response.raise_for_status()

    data = response.json()
    sunrise = int(data["sunrise"].split("T")[1].split("+")[0])
    sunset = int(data["sunset"].split("T")[1].split("+")[0])

    time_now = datetime.now().hour


    if time_now >= sunset or time_now <= sunrise:
        return  True



def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject:Look Up\n\nThe ISS in above you in the sky."
            )


