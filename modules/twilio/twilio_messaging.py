from __future__ import print_function

# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
from modules.twilio import twilio_account_details
from database.sms_database import SmsDatabase


class Messaging:
    def __init__(self):
        # Configure HTTP basic authorization: BasicAuth
        account_sid = twilio_account_details.account_sid
        auth_token = twilio_account_details.auth_token
        self._client = Client(account_sid, auth_token)
        self._db = SmsDatabase()

    def send_message(self, to: str, body: str):

        message = self._client.messages \
            .create(
                body=body,
                from_=twilio_account_details.phone_from,
                to=to,
            )
        self._db.insert_sms_data(to, body)
        print(message.sid)
