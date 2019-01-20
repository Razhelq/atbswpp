# text_myself.py - Defines the text_myself() function that texts a message passed to it as a string.


from twilio.rest import Client


account_SID = ''
auth_token = ''
my_number = ''
twilio_number = ''


def text_myself(message):
        twilioCli = Client(account_SID, auth_token)
        twilioCli.messages.create(body=message, from_=twilio_number, to=my_number)
