import requests
from day35.getCoordinates import locationCoordinates

lat, long, city, state = locationCoordinates()

apikey = ""
getKey = f"http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey={apikey}&q={lat},{long}"

locationParams = {
    'apikey': apikey,
    'q': f"{lat}, {long}"
}
response = requests.get(getKey, params=locationParams)
response.raise_for_status()
locationData = response.json()
key = locationData['Key']

endpoint_url = f"http://dataservice.accuweather.com/forecasts/v1/daily/1day/{key}"
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
daily_forecasts = weather_data.get('DailyForecasts', [])
weather_slice = daily_forecasts[0]
day_forecast = weather_slice.get('Day', {})
thunderProbability = day_forecast['ThunderstormProbability']
print(thunderProbability)