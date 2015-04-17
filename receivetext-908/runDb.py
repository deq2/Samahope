from flask import Flask, request, redirect, make_response
import twilio.twiml
from datetime import datetime, timedelta
from google.appengine.ext import ndb

class Row(ndb.Model):
  """Models an individual Guestbook entry with content and date."""
  content = ndb.StringProperty()

  @classmethod
  def query_book(cls, ancestor_key):
    return cls.query(ancestor=ancestor_key).order(-cls.date)

 
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def run():
    """Respond to incoming calls with a simple text message."""

    resp = twilio.twiml.Response()
    echo = request.values.get("Body")
    resp.message(echo)
    row = Row(parent=ndb.Key("Key"), content = echo)
    row.put()

    return str(resp)
 
if __name__ == "__main__":
    app.run(debug=True)