#!flask/bin/python
import os
from flask import Flask,jsonify
from time import sleep
from extendtoken import extendtoken
from webhook import posttoSlack
import requests

try:
	from init import *	#for local env variables
except:
	pass

app = Flask(__name__)

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
    payload={"text": access_token+" "+str(flag)}
    response = requests.post(slack_url,json.dumps(payload))
    exit()


@app.route('/')
def index():
    """Index Page"""
    global packetm
    global packetn
    global count

    packetm,packetn = posttoSlack(slack_url,app_token,access_token,packetm,packetn,count)
    count += 1
    print "Polled: ",count # check logs

    return jsonify(msg="thank you!")


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0',port=port,debug=True)
