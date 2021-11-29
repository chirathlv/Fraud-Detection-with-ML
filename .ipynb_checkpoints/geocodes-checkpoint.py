from geopy.geocoders import Nominatim
import pandas as pd

geolocator = Nominatim(user_agent='http')

def add_coordinates(i):
    location = geolocator.geocode(i)
    return location.raw['lat'], location.raw['lon']