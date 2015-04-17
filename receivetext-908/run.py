from flask import Flask, request, redirect, make_response
import twilio.twiml
from datetime import datetime, timedelta
from google.appengine.ext import ndb
 
app = Flask(__name__)
 
@app.route("/", methods=['GET', 'POST'])
def run():
    """Respond to incoming calls with a simple text message."""

    resp = twilio.twiml.Response()
    resp.message(request.values.get("Body"))

    return str(resp)
 
if __name__ == "__main__":
    app.run(debug=True)