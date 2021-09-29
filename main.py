# import smtplib
#
# my_email = "tloatmancodes@gmail.com"
# password =
#
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="tloatman77@yahoo.com",
#         msg="Subject:Hello\n\nThis is the body of my email."
#     )

import datetime as dt
import smtplib
import random

now = dt.datetime.now()
week_day = now.weekday()
monday = 2

if week_day == monday:
    my_email = "tloatmancodes@gmail.com"
    password = ""

    with open("quotes.txt", "r") as file:
        content = file.readlines()
        quote = random.choice(content)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="tloatman77@yahoo.com",
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )

