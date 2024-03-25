import requests
def locationCoordinates():
    try:
        response = requests.get('https://ipinfo.io')
        data = response.json()
        location = data['loc'].split(',')
        lat, long = float(location[0]), float(location[1])
        city = data.get('city', 'Unknown')
        state = data.get('region', 'Unknown')
        return lat, long, city, state
    except:
        print("Connection lost!")
        exit()
