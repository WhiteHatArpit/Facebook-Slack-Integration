from apscheduler.schedulers.blocking import BlockingScheduler
import os
from extendtoken import extendtoken
from webhook import posttoSlack

#for running on local, make a file 'init.py' where you set the environ variables
#from init import *

import logging
logging.basicConfig()

sched = BlockingScheduler()
packetm = ""
packetn = ""
count = 0

slack_url = os.environ['slack_url']
app_id = os.environ['app_id']
app_secret = os.environ['app_secret']
app_token = app_id + "|" + app_secret
access_token = os.environ['access_token']

# extend token if short lived, check for permissions
access_token,flag = extendtoken(app_token,access_token)

# report back and exit if bad token
if flag==0:
    packetm = access_token
    posttoSlack(slack_url,app_token,access_token,packetm,packetn,count,0)
    exit()

# polls every 10mins for messages, 60mins for notification
@sched.scheduled_job('interval', minutes=10)
def timed_job():
    global count
    global packetm
    global packetn
    
    packetm,packetn = posttoSlack(slack_url,app_token,access_token,packetm,packetn,count,1)
    count += 1
    print "Polled: ",count # check logs
    
sched.start()
