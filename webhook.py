import requests
import json
from parse import parse,parsenotif
from fetch import fetch,fetchnotif

# fetch, parse and post to slack
def posttoSlack(slack_url,app_token,access_token,packetm,packetn,count):
	
	# for debugging token, check if valid
	debug_url ="https://graph.facebook.com/debug_token?input_token="+ access_token +"&access_token=" + app_token
	prev_packetm = packetm
	prev_packetn = packetn
	
	try:
		response = requests.get(debug_url)
		data = json.loads(response.text)

		# validation of token
		if 'error' in data.keys():
			packetm = "access_token not valid"
		else:
			# fetch messages data
			try:
				data = fetch(access_token) 
			except:
				packetm = "Couldnt Fetch"
			# parse fetched message data
			try:
				packetm = parse(data)
			except:
				packetm = "Couldnt Parse"

			# change this if you need to get updated for notifications more frequently
			if count % 6 == 0:
				# fetch notifications data 
				try:
					data = fetchnotif(access_token)
				except:
					packetn = "Couldnt Fetch Notif"
				# parse notifications data
				try:
					packetn = parsenotif(data)
				except:
					packetn = "Couldnt Parse Notif"


	except:
		packetm = "Couldnt Debug"	

	# prepare packet with messages and notifications
	if count % 6 == 0:
		# post to slack if not same as earliar
		if packetn+packetm != prev_packetn+prev_packetm:
			payload={"text": packetn+packetm }
			response = requests.post(slack_url,json.dumps(payload))

	# prepare packet with messages only	
	else:
		# post to slack if not same as earliar
		if packetm != prev_packetm:
			payload={"text": packetm }
			response = requests.post(slack_url,json.dumps(payload))
		
	return packetm,packetn

