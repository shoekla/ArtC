from twilio.rest.resources import Connection
from twilio.rest.resources.connection import PROXY_TYPE_HTTP
from twilio.rest import TwilioRestClient


# Find these values at https://twilio.com/user/account
account_sid = "ACa4c3ccef1ad1756610b63eac37ffa0ce"
auth_token = "879040038e39074537d376416659b1e6"
client = TwilioRestClient(account_sid, auth_token)

def sendMessage(mess,phone):
	message = client.messages.create(to="+1"+phone, from_="+18326481563",
                                     body="\n\n\t"+mess)



call = client.calls.create(to="+17132317925",  # Any phone number
                           from_="+18326481563", # Must be a valid Twilio number
                           url="http://abirshukla.pythonanywhere.com/dial/")
print(call.sid)























































