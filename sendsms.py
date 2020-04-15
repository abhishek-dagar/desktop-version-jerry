from twilio.rest import Client
import json
with open("JSON_FILE\\info.json") as w:
	data=json.load(w)
for info in data['tokken']:
	account_sid = info['account_sid'] # Found on Twilio Console Dashboard
	auth_token = info['auth_token'] # Found on Twilio Console Dashboard
	myPhone = '+919643501840' # Phone number you used to verify your Twilio account
	TwilioNumber = info['TwilioNumber'] # Phone number given to you by Twilio
def sms(ph_nuber,msg):
	client = Client(account_sid, auth_token)
	client.messages.create(to=ph_nuber,from_=TwilioNumber,body=msg)
