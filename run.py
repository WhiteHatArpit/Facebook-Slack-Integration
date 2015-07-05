#!flask/bin/python
import os
from flask import Flask
from time import sleep
from extendtoken import extendtoken
from webhook import posttoSlack
import requests

#for running on local, make a file 'init.py' where you set the environ variables
#from init import *

port = int(os.environ.get('PORT', 8000))
app = Flask(__name__)

@app.route('/')
def index():
    """Index Redirect Page"""
    return '''yo'''



@app.route('/run')
def run():
    """Visit to run integration"""

    packetm = ""
    packetn = ""
    count = 0

    slack_url = os.environ['slack_url']
    app_id = os.environ['app_id']
    app_secret = os.environ['app_secret']
    app_token = app_id + "|" + app_secret
    access_token = os.environ['access_token']

    # extend token if short lived, check for permissions
    access_token,flag = extendtoken(app_id,app_secret,access_token)

    # report back and exit if bad token
    if flag==0:
        packetm = access_token
        posttoSlack(slack_url,app_token,access_token,packetm,packetn,count,0)
        exit()

    heroku_url = os.environ['heroku_url']

    # polls every 10mins for messages, 60mins for notification
    while True:

        temp = requests.get(heroku_url)

        packetm,packetn = posttoSlack(slack_url,app_token,access_token,packetm,packetn,count,1)
        count += 1
        print "Polled: ",count # check logs
        
        sleep(60*10)

    return '''running'''



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=port,debug=True)
