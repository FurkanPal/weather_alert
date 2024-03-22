from geopy.geocoders import Nominatim

import requests

# def get_user_location():
#     locator = Nominatim(user_agent="user_location")
#     location = locator.geocode('')
#     if location:
#         return location.latitude, location.longitude
#     else:
#         return None, None
#
# latitude, longitude = get_user_location()
location = "349727"
endpoint_url = f"http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/{location}"
apikey = ""
query_params = {
    'apikey': f'{apikey}',
    'language': 'en-us',
    'details': 'true',
    'metric': 'true'
}

response = requests.get(endpoint_url, params=query_params)
response.raise_for_status()
data = response.json()
weather_data = response.json()
weather_slice = weather_data[0]
thunderProbability = weather_slice['ThunderstormProbability']