# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC5f5ccd1c87d81fe182e03012e447e1f5"
auth_token  = "52852f1100ab11967425947d24b61534"
client = TwilioRestClient(account_sid, auth_token)
 
# A list of message objects with the properties described above
messages = client.messages.list()

for message in messages:
	print message.body