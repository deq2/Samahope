from flask import Flask, request, redirect, session
import twilio.twiml
 
# The session object makes use of a secret key.
SECRET_KEY = 'a secret key'
app = Flask(__name__)
app.config.from_object(__name__)

FIELDS = ['Date','Id','Child name','Child sex','Date of birth','Caregiver',
		  'Relationship','Caregiver age','District','Sub country']
PROMPTS =  ['Date of Registration', 
			'Unique Identity Number', 
			'Name of Child',
			"Child's sex (M/F)",
			"Child's date of birth",
			'Name of caregiver',
			'Relationship with the child',
			'Age of caregiver',
			'District where the OCV resides',
			'Sub country where the OCV resides']


# FIELDS = FIELDS[0:2]
# PROMPTS = PROMPTS[0:2]
 
@app.route("/", methods=['GET', 'POST'])
def run():	
	stage = session.get('stage', 0)
	message = ''

	body = request.values.get("Body")
	if body <> None and body.upper() == 'RESET':
		stage = 0
		message = 'Record reset. '

	# Save the new counter value in the session
	session['stage'] = stage + 1

	if stage > 0:
		session[FIELDS[stage - 1]] = body

	if stage == 0:
		message += 'Please enter the following items:\n'

	if stage < len(FIELDS):
		message += str(stage+1) + '. ' + PROMPTS[stage] 
	# increment the counter

	if (stage) == len(FIELDS):
		message = "Record complete. You have submitted the following items:\n"
		session['stage'] = 0
		for i in range(len(FIELDS)):
			message += PROMPTS[i] + ": " + session[FIELDS[i]] + "\n"

	resp = twilio.twiml.Response()
	resp.sms(message)

	return str(resp)
 
if __name__ == "__main__":
	app.run(debug=True)



