import requests
import json
import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from twilio.rest import Client

import time

#dt = str(datetime.datetime.utcnow().isoformat()) + "Z"

import api
from config import wkKey
from config import twilAccSID
from config import twilAuthTok
from config import twilNum
from config import userNum

twilClient = Client(twilAccSID, twilAuthTok)


exit()


#CHECKING LOOP SYSTEM
print("Start")

def jobTest():
    print(datetime.datetime.now())

jobTest()

scheduler = BackgroundScheduler()
scheduler.start()
scheduler.add_job(jobTest, 'interval', seconds=1)


time.sleep(5)

print("Stop")
