import requests
from twilio.rest import Client
import os

from day35.get_user_location import get_user_location

# Locate user
latitude, longtitude = get_user_location()


OWM_endpoints = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("api_key")
weather_params = {
    "lat": latitude,
    "lon": longtitude,
    "appid": api_key,
    "exclude": "current, minutely, daily"
}

storm = False
will_rain = False
clear = False
# Twillio
account_sid = "[]"
auth_token = os.environ.get("token")

# Weather
response = requests.get(OWM_endpoints, params=weather_params)
response.raise_for_status()
weather_data = response.json()
wearher_slice = weather_data["hourly"][0:12]

for hourly in wearher_slice:
    condition_code = hourly["weather"][0]["id"]
    if 200 <= condition_code <= 230:
        storm = True
    elif condition_code >= 700:
        will_rain = True
    elif condition_code == 800:
        clear = True

if will_rain == True:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="",
        from_="",
        to=""
    )
    print(message.status)
elif storm:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="⚠️ Severe Storm Alert ⚠️\nStay Safe!\n- [Your Name/Organization]",
        from_="",
        to=""
    )
    print(message.status)
