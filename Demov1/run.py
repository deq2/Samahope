from flask import Flask, request, redirect, make_response
import twilio.twiml
from datetime import datetime, timedelta
 
app = Flask(__name__)
 
@app.route("/", methods=['GET', 'POST'])
def run():
    """Respond to incoming calls with a simple text message."""

    resp = twilio.twiml.Response()
    resp.message("sup?")

    return str(resp)
 
if __name__ == "__main__":
    app.run(debug=True)