from os import curdir
from typing import NewType
import pywhatkit
import time
import datetime


print("Welcome to whatsapp automatic Spam!")
crntycod = int(input("Please enter the country code of your phone number in the format \"49\": "))
tel = int(input("Please enter your phone number: "))
message = str(input("Enter your message: "))
interval = int(input("Enter Sending interval in mins !cannot be smaller than 2 mins! : "))
amount = int(input("Enter amount of messages: "))

date = datetime.datetime.fromordinal(730920)
nexttime = date.today()
for i in range(0,amount):
    nexttime = nexttime + datetime.timedelta(minutes=interval)
    print(f"The next message will be sent at {nexttime.hour}: {nexttime.minute}")
    pywhatkit.sendwhatmsg(f"+{crntycod}{tel}",message,nexttime.hour,nexttime.minute)


print("Done!")
