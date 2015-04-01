To send a message:
	- Open send_message.py
	- Edit recipient phone # (e.g. +18054059856) and message body
	- Run script from command line ("python send_message.py")

To set-up an automatic response:
	- Open run.py
	- Edit response message 
	- Run script from command line. This should create an html-like file on your local server (e.g. http://127.0.0.1:5000/)
	- Make local server accessible remotely by running ./ngrok + address (e.g. ./ngrok 5000)
	- Connect the ngrok web address (e.g. http://dba02a1.ngrok.com) to the number in our Twilio account (Numbers -> 8056018122 -> Messaging -> Request URL)