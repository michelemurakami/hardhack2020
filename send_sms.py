# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACf1fac71b61ce2ecc7f651b9e7d0f7116'
auth_token = 'ea984cc8c5c51f7493c8171e2dd05422'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+12053950706',
                     to='+16266441183'
                 )
print(message.sid)
