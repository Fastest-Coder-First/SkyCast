import geocoder
from geopy.geocoders import Nominatim

class GeolocationModel:
    def __init__(self):
        self.geolocator = Nominatim(user_agent="my-app")

    @staticmethod
    def get_current_location():
        # Use geocoder to get the current location
        g = geocoder.ip('me')
        if g.latlng:
            latitude, longitude = g.latlng
            return latitude, longitude
        else:
            return None

    def get_location_by_name(self, location):
        location_data = self.geolocator.geocode(location)

        if location_data is None:
            return None

        latitude = location_data.latitude
        longitude = location_data.longitude
        return latitude, longitude
