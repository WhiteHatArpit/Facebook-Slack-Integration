import requests
import json
import string


def extendtoken(app_token,access_token):
	
	debug_url ="https://graph.facebook.com/v2.2/debug_token?input_token="+ access_token +"&access_token=" + app_token
	
	try:
		response = requests.get(debug_url)
		data = json.loads(response.text)

		if 'error' in data['data'].keys():
			access_token = "access_token not valid"
			return access_token,0	
			
		else:
			if 'read_stream' not in data['data']['scopes']:
				access_token = "Please add 'read_stream' permission"
				return access_token,0	
			if 'manage_notifications' not in data['data']['scopes']:
				access_token = "Please add 'manage_notifications' permission"
				return access_token,0
			if 'read_mailbox' not in data['data']['scopes']:
				access_token = "Please add 'read_mailbox' permission"
				return access_token,0			
			
			if 'issued_at' in data['data'].keys():
				return access_token,1
			else:
				url = "https://graph.facebook.com/v2.2/oauth/access_token?grant_type=fb_exchange_token&client_id=" + app_token[:16] + "&client_secret=" + app_token[17:] + "&fb_exchange_token=" + access_token
				response = requests.get(url)
				data = response.content
				pos = string.index(data,'&')
				access_token = data[13:pos]
				return access_token,1	
			
	except:
		access_token = "Couldnt Debug"
		return access_token,0	
			



