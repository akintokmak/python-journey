import smtplib
import datetime as dt
import random
import os

#Email
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt", "r") as quote_file:
        all_quotes = quote_file.readlines()
        random_quotes = random.choice(all_quotes)
        print(random_quotes)


    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:  # Gmail
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="gameboom45@gmail.com",
            msg=f"Subject:Monday Motivation"
                f"\n\n"
                f"{random_quotes}")

        connection.close()



