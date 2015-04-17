from flask import Flask, request, redirect, session
import twilio.twiml
 
# The session object makes use of a secret key.
SECRET_KEY = 'a secret key'
app = Flask(__name__)
app.config.from_object(__name__)
 
@app.route("/", methods=['GET', 'POST'])
def run():
    """Respond with the number of text messages sent between two parties."""
 
    counter = session.get('counter', 0)
 
    # increment the counter
    counter += 1
 
    # Save the new counter value in the session
    session['counter'] = counter

    message = str(counter)

    # counter = session.get('echo', 0)
    # if session.has_key('echo2'):
    #     session['echo2'] += ' ' + request.values.get('Body')
    # else: 
    #     session['echo2'] = 'hello'

    # message = session['echo2']

    # message = session.get('echo3', 'hello')
    # session['echo3'] += ' ' + request.values.get('Body')

    # if request.values.get('Body') == 'reset':
    #     message = 'reset'
    #     session['echo'] = None
    # # elif session.has_key['echo'] and session['echo'] <> None:
    # #     message = session['echo']
    # #     session['echo'] += request.values.get('Body')
    # else:
    #     message = 'hello'
    #     session['echo'] = request.values.get('Body')
 
    # Save the new counter value in the session
    # session['echo'] += ' ' + request.values.get('Body')
 
    # message = 'hello'
    resp = twilio.twiml.Response()
    resp.sms(message)
 
    return str(resp)
 
if __name__ == "__main__":
    app.run(debug=True)

# from flask import Flask, request, redirect, make_response, session
# import twilio.twiml
# from datetime import datetime, timedelta
# from google.appengine.ext import ndb
 
# # The session object makes use of a secret key.
# SECRET_KEY = 'a secret key'
# app = Flask(__name__)
# app.config.from_object(__name__)

# @app.route("/", methods=['GET', 'POST'])
# def run():
#     """Respond to incoming calls with a simple text message."""

#     # session['counter'] = 0
# 	# counter = session.get('counter', 0)
 
#     # # increment the counter
#     # counter += 1
    
#     # # Save the new counter value in the session
#     # session['counter'] = counter
    
#     resp = twilio.twiml.Response()
#     # resp.message(request.values.get("Body"))

#     if session.has_key('counter'): 
#         resp.message("hello"):
#     else:
#         resp.message("goodbye")

#     return str(resp)
 
# if __name__ == "__main__":
#     app.run(debug=True)
