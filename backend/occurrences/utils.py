import os
from geopy.geocoders import Nominatim


def getCoordsFromAddress(self, address):
    geolocator = Nominatim(user_agent=os.getenv('GOOGLE_APPNAME'))
    coordinates = geolocator.geocode(address)
    pnt = 'POINT('+ str(coordinates.latitude) + ' ' + str(coordinates.longitude) + ')'
    return pnt


def getLocationFromCoords(self, coords):
    geolocator = Nominatim(user_agent=os.getenv('GOOGLE_APPNAME'))
    location =geolocator.reverse(str(coords[0]) + ', ' + str(coords[1]))
    return location.address
