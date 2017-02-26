from flask import Flask, request, redirect
import twilio.twiml
from twilio.rest import TwilioRestClient
import art

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def hello_monkey():    
	resp = twilio.twiml.Response()
	message_body = request.form['Body']
	num,loc = art.getPhoneNumberForMueseum(message_body)
	resp.message(num+"\n\n"+loc)
	from_number = request.values.get('From', None)

	account_sid = "ACa4c3ccef1ad1756610b63eac37ffa0ce"
	auth_token = "879040038e39074537d376416659b1e6"
	client = TwilioRestClient(account_sid, auth_token)

	client.calls.create(to=from_number,  # Any phone number
						from_="+18326481563", # Must be a valid Twilio number
						url="http://abirshukla.pythonanywhere.com/dial/" + num)

	return str(resp)

@app.route("/dial/<num>", methods=['GET', 'POST'])
def redPhone(num):
	resp = twilio.twiml.Response()
	resp.dial("+1"+num)
	return str(resp)

if __name__ == "__main__":
    app.run(debug=True)