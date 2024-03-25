import time

from day35.get_user_location import thunderProbability
from twilioPackage import sendSms


probability = thunderProbability
while True:
    if probability >= 70:
        print("⚠️ Severe Storm Alert ⚠️\nStay Safe!\n- [Your Name/Organization]")
        sendSms()
    time.sleep(3600)

