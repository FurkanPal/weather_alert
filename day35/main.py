import time

from day35 import twilioPackage
from day35.get_user_location import weather_slice
from twilioPackage import sendSms


probability = weather_slice['ThunderstormProbability']
print(twilioPackage.sendSms())
while True:
    if probability == 1:
        sendSms()
    time.sleep(3600)
