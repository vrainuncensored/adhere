from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""

    body = request.values.get('Body', None)

    # Start our TwiML response
    resp = MessagingResponse()

    if body == 'Y' or body == 'y' or body == "Yes" or body == "yes":
        resp.message("That's great! Keep up the great work")
    elif body == 'N' or body == 'n' or body == "No" or body == "no": 
        resp.message("It's the thought that counts. You can do it, but don't worry, we'll remind you in 30 minutes")
    else:
        resp.message("Sorry, we can't make sense of what you texted back. The accepted format is Yes or No")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)