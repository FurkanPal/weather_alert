from geopy.geocoders import Nominatim

def get_user_location():
    locator = Nominatim(user_agent="user_location")
    location = locator.geocode('')
    if location:
        return location.latitude, location.longitude
    else:
        return None, None
