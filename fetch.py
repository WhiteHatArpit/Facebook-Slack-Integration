import requests
import json

# fetch messages data
def fetch(access_token):
	
	fields = "name,inbox{from,unread,unseen,comments{message,from},to}"
	url = "https://graph.facebook.com/v2.3/me?access_token="+access_token+"&fields="+fields

	response = requests.get(url)
	data = json.loads(response.text)

	return data

# fetch notifications data
def fetchnotif(access_token):
	
	fields = "name,notifications{from,title,unread}"
	url = "https://graph.facebook.com/v2.3/me?access_token="+access_token+"&fields="+fields

	response = requests.get(url)
	data = json.loads(response.text)

	return data

