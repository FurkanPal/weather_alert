from twilio.rest import Client
import os

# Twillio
account_sid = ""
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
UserPhoneNumber = ""
def sendSms():
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="⚠️ Severe Storm Alert ⚠️\nStay Safe!\n- [Your Name/Organization]",
        from_=f"{auth_token}",
        to=f"{UserPhoneNumber}"
    )
    print(f"Warning Sms sent to {message.to}")
