# Tabulate for table formats
from tabulate import tabulate

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

class Weather:

    # Contains variables to be accessed outside of the Weather class for the Wellness implimentation
    def __init__(self):

        # Hourly Variables
        self.HourlyTemp = None
        self.HourlyFeelsLike = None
        self.HourlyWeatherCode = None
        self.HourlyPrecip = None
        self.HourlyWindSpeed = None
        self.HourlyWindDir = None
        self.HourlyWindGusts = None

        # Daily Variables
        self.DailyWeatherCode = None
        self.DailyTempMax = None
        self.DailyTempMin = None
        self.DailyPrecipHours = None
        self.DailyPrecipProb = None

        # Current Variables
        self.CurrTemp = None
        self.CurrFeelsLike = None
        self.CurrIsDay = None
        self.CurrWeatherCode = None
        self.CurrWindSpeed = None
        self.CurrWindDir = None


    # View Forecast
    def ForecastDaily(self, lat, long):
        # For weather codes, refer to https://www.nodc.noaa.gov/archive/arc0021/0002199/1.1/data/0-data/HTML/WMO-CODE/WMO4677.HTM
        # -----------------------------------

        # Make sure all required weather variables are listed here
        # The order of variables in hourly or daily is important to assign them correctly below
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
        "latitude": lat,
        "longitude": long,
        "daily": ["weather_code", "temperature_2m_max", "temperature_2m_min", "precipitation_hours", "precipitation_probability_max"],
        "temperature_unit": "fahrenheit",
        "wind_speed_unit": "mph",
        "precipitation_unit": "inch",
        "timezone": "auto",
        "forecast_days": 7
        }
        responses = openmeteo.weather_api(url, params=params)

        # Process first location. Add a for-loop for multiple locations or weather models
        response = responses[0]
        print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
        print(f"Elevation {response.Elevation()} m asl")
        print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
        print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

        # Process daily data. The order of variables needs to be the same as requested.
        daily = response.Daily()
        daily_weather_code = daily.Variables(0).ValuesAsNumpy()
        daily_temperature_2m_max = daily.Variables(1).ValuesAsNumpy()
        daily_temperature_2m_min = daily.Variables(2).ValuesAsNumpy()
        daily_precipitation_hours = daily.Variables(3).ValuesAsNumpy()
        daily_precipitation_probability_max = daily.Variables(4).ValuesAsNumpy()

        daily_data = {"date": pd.date_range(
            start = pd.to_datetime(daily.Time(), unit = "s", utc = True),
            end = pd.to_datetime(daily.TimeEnd(), unit = "s", utc = True),
            freq = pd.Timedelta(seconds = daily.Interval()),
            inclusive = "left"
        )}

        daily_data["weather_code"] = daily_weather_code
        daily_data["temperature_2m_max"] = daily_temperature_2m_max
        daily_data["temperature_2m_min"] = daily_temperature_2m_min
        daily_data["precipitation_hours"] = daily_precipitation_hours
        daily_data["precipitation_probability_max"] = daily_precipitation_probability_max

        daily_dataframe = pd.DataFrame(data = daily_data)
        print(tabulate(daily_dataframe, headers="keys", tablefmt="grid"))


        # For public variables for outside access
        # ------------------------------------------------------------
        daily_data["weather_code"] = self.DailyWeatherCode
        daily_data["temperature_2m_max"] = self.DailyTempMax
        daily_data["temperature_2m_min"] = self.DailyTempMin
        daily_data["precipitation_hours"] = self.DailyPrecipHours
        daily_data["precipitation_probability_max"] = self.DailyPrecipProb


    # View Hourly Forecast
    def ForecastHourly(self, lat, long):
        
        # Make sure all required weather variables are listed here
        # The order of variables in hourly or daily is important to assign them correctly below
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": lat,
            "longitude": long,
            "hourly": ["temperature_2m", "apparent_temperature", "precipitation_probability", "weather_code", "wind_speed_10m", "wind_direction_10m", "wind_gusts_10m"],
            "temperature_unit": "fahrenheit",
            "wind_speed_unit": "mph",
            "precipitation_unit": "inch",
            "timezone": "auto",
            "forecast_days": 1
        }
        responses = openmeteo.weather_api(url, params=params)

        # Process first location. Add a for-loop for multiple locations or weather models
        response = responses[0]
        print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
        print(f"Elevation {response.Elevation()} m asl")
        print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
        print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

        # Process hourly data. The order of variables needs to be the same as requested.
        hourly = response.Hourly()
        hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
        hourly_apparent_temperature = hourly.Variables(1).ValuesAsNumpy()
        hourly_precipitation_probability = hourly.Variables(2).ValuesAsNumpy()
        hourly_weather_code = hourly.Variables(3).ValuesAsNumpy()
        hourly_wind_speed_10m = hourly.Variables(4).ValuesAsNumpy()
        hourly_wind_direction_10m = hourly.Variables(5).ValuesAsNumpy()
        hourly_wind_gusts_10m = hourly.Variables(6).ValuesAsNumpy()

        hourly_data = {"date": pd.date_range(
            start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
            end = pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
            freq = pd.Timedelta(seconds = hourly.Interval()),
            inclusive = "left"
        )}

        hourly_data["temperature_2m"] = hourly_temperature_2m
        hourly_data["apparent_temperature"] = hourly_apparent_temperature
        hourly_data["precipitation_probability"] = hourly_precipitation_probability
        hourly_data["weather_code"] = hourly_weather_code
        hourly_data["wind_speed_10m"] = hourly_wind_speed_10m
        hourly_data["wind_direction_10m"] = hourly_wind_direction_10m
        hourly_data["wind_gusts_10m"] = hourly_wind_gusts_10m

        hourly_dataframe = pd.DataFrame(data = hourly_data)
        print(tabulate(hourly_dataframe, headers="keys", tablefmt="grid"))


        # For public variables for outside access
        # ------------------------------------------------------------
        hourly_data["temperature_2m"] = self.HourlyTemp
        hourly_data["apparent_temperature"] = self.HourlyFeelsLike
        hourly_data["precipitation_probability"] = self.HourlyPrecip
        hourly_data["weather_code"] = self.HourlyWeatherCode
        hourly_data["wind_speed_10m"] = self.HourlyWindSpeed
        hourly_data["wind_direction_10m"] = self.HourlyWindDir
        hourly_data["wind_gusts_10m"] = self.HourlyWindSpeed


    # View Current Weather
    def ViewCurrWeather(self, lat, long):
        # Make sure all required weather variables are listed here
        # The order of variables in hourly or daily is important to assign them correctly below
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": lat,
            "longitude": long,
            "current": ["temperature_2m", "apparent_temperature", "is_day", "weather_code", "wind_speed_10m", "wind_direction_10m"],
            "temperature_unit": "fahrenheit",
            "wind_speed_unit": "mph",
            "precipitation_unit": "inch",
            "timezone": "auto"
        }
        responses = openmeteo.weather_api(url, params=params)

        # Process first location. Add a for-loop for multiple locations or weather models
        response = responses[0]
        print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
        print(f"Elevation {response.Elevation()} m asl")
        print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
        print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")


        # Current values. The order of variables needs to be the same as requested.
        current = response.Current()

        current_temperature_2m = current.Variables(0).Value()

        current_apparent_temperature = current.Variables(1).Value()

        current_is_day = current.Variables(2).Value()

        current_weather_code = current.Variables(3).Value()

        current_wind_speed_10m = current.Variables(4).Value()

        current_wind_direction_10m = current.Variables(5).Value()

        print(f"Current time {current.Time()}")

        print(f"Current temperature_2m {current_temperature_2m}")
        print(f"Current apparent_temperature {current_apparent_temperature}")
        print(f"Current is_day {current_is_day}")
        print(f"Current weather_code {current_weather_code}")
        print(f"Current wind_speed_10m {current_wind_speed_10m}")
        print(f"Current wind_direction_10m {current_wind_direction_10m}")


        # For public variables for outside access
        # ------------------------------------------------------------
        self.CurrTemp = current_temperature_2m
        self.CurrFeelsLike = current_apparent_temperature
        self.CurrIsDay = current_is_day
        self.CurrWeatherCode = current_weather_code
        self.CurrWindSpeed = current_wind_speed_10m
        self.CurrWindDir = current_wind_direction_10m


    # Set Current Location
    def SetCurrLoc(self):

        # Use geopy to get lat and long
        loc = {}
        lat = 0.0
        long = 0.0

        # City conversion still in progress !!!!!!!!!!!!!!!
        
        isValid = False

        while isValid == False:
            useCurrLoc = input('Do you want to use your current location? (yes/no/cancel): ')
            if useCurrLoc.lower() == 'yes':
                loc = geocoder.ip('me')

                if loc.ok:
                    lat = {loc.latlng[0]}
                    long = {loc.latlng[1]}
                    isValid = True
                else:
                    print("Could not retrieve current location")
            
            elif useCurrLoc.lower() == 'no':
                city = input("Enter City: ")
                loc = geocoder.osm(city)

                if loc.ok:
                    lat = {loc.latlng[0]}
                    long = {loc.latlng[1]}
                    isValid = True
                else:
                    print("City could not be found. Try Again or choose your location.")
            elif useCurrLoc.lower() == 'cancel':
                raise Exception("Canceled")

        return lat, long



