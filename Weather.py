# Weather API
import openmeteo_requests

import requests_cache
import pandas as pd
from retry_requests import retry

# Location API
import geocoder

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)


# View Forecast
def Forecast(lat, long):
    # Use Weather API to implement forecast
    return 0


# View Current Weather
def ViewCurrWeather(lat, long):
    # Use Weather API to implement current weather
    return 0


# Set Current Location
def SetCurrLoc():

    # Use geopy to get lat and long
    loc = {}
    lat = 0.0
    long = 0.0

    useCurrLoc = input('Do you want to use your current location? (yes/no): ')
    
    if useCurrLoc.toLower() == 'yes':
        loc = geocoder.ip('me')

        if loc.ok:
            lat = {loc.latlng[0]}
            long = {loc.latlng[1]}
        else:
            print("Could not retrieve current location")
    
    else:
        city = input("Enter City: ")
        loc = geocoder.osm(city)

        if loc.ok:
            lat = {loc.latlng[0]}
            long = {loc.latlng[1]}
        else:
            print("City could not be found")

    return lat, long
        

if __name__ == "__main__":

    lat, long = SetCurrLoc()
    print(f'{lat}, {long}')        
    



