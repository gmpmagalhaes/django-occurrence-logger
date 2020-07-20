import os
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent=os.getenv('GOOGLE_APPNAME'))
    
def getCoordsFromAddress(address):
    coordinates = geolocator.geocode(address)
    return 'POINT('+ str(coordinates.longitude) + ' ' + str(coordinates.latitude) + ')'
 

def getLocationFromCoords(coords):
    coords = str(coords[0]) + ', ' + str(coords[1])
    location = geolocator.reverse( coords )
    return location.address