# Tabulate for table formats
from tabulate import tabulate

# Weather API
import openmeteo_requests

import requests_cache
import pandas as pd
from retry_requests import retry

# Location API
import geocoder

# Translates Weather Codes
#from WeatherCodeTranslations import WeatherCodeTranslations

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

class Weather:


    # View Forecast
    def ForecastDaily(lat, long):
        # For weather codes, refer to https://www.nodc.noaa.gov/archive/arc0021/0002199/1.1/data/0-data/HTML/WMO-CODE/WMO4677.HTM
        # -----------------------------------

        # Make sure all required weather variables are listed here
        # The order of variables in hourly or daily is important to assign them correctly below
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": lat,
            "longitude": long,
            "daily": ["weather_code", "temperature_2m_max", "temperature_2m_min", "precipitation_probability_max", "wind_speed_10m_max"],
            "temperature_unit": "fahrenheit",
            "wind_speed_unit": "mph",
            "precipitation_unit": "inch",
            "timezone": "America/Chicago"
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
        daily_precipitation_probability_max = daily.Variables(3).ValuesAsNumpy()
        daily_wind_speed_10m_max = daily.Variables(4).ValuesAsNumpy()

        daily_data = {"date": pd.date_range(
            start = pd.to_datetime(daily.Time(), unit = "s", utc = True),
            end = pd.to_datetime(daily.TimeEnd(), unit = "s", utc = True),
            freq = pd.Timedelta(seconds = daily.Interval()),
            inclusive = "left"
        )}

        daily_data["weather_code"] = daily_weather_code
        daily_data["temperature_2m_max"] = daily_temperature_2m_max
        daily_data["temperature_2m_min"] = daily_temperature_2m_min
        daily_data["precipitation_probability_max"] = daily_precipitation_probability_max
        daily_data["wind_speed_10m_max"] = daily_wind_speed_10m_max

        daily_dataframe = pd.DataFrame(data = daily_data)
        print(tabulate(daily_dataframe, headers="keys", tablefmt="grid"))

        return {"DailyWeatherCode": daily_weather_code, "DailyTempMax": daily_temperature_2m_max, "DailyTempMin": daily_temperature_2m_min, 
                "DailyPrecipProb": daily_precipitation_probability_max, "DailyWindSpeed": daily_wind_speed_10m_max}


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

        return {"HourlyTemp": hourly_temperature_2m, "HourlyFeelsLike": hourly_apparent_temperature, "HourlyPrecipProb": hourly_precipitation_probability, "HourlyWeatherCode": hourly_weather_code,
                    "HourlyWindSpeed": hourly_wind_speed_10m, "HourlyWindDir": hourly_wind_direction_10m, "HourlyWindGusts": hourly_wind_gusts_10m}



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

        print(f"Current temperature: {current_temperature_2m}")
        print(f"Current feels like: {current_apparent_temperature}")
        print(f"Current is_day: {current_is_day}")
        print(f"Current weather_code: {current_weather_code}")
        print(f"Current wind speed: {current_wind_speed_10m}")
        print(f"Current wind direction: {current_wind_direction_10m}")

        return {"CurrTemp": current_temperature_2m, "CurrFeelsLike": current_apparent_temperature, "CurrIsDay": current_is_day, "CurrWeatherCode": current_weather_code,
                "CurrWindSpeed": current_wind_speed_10m, "CurrWindDir": current_wind_direction_10m}


    # Set Current Location
    @staticmethod
    def SetCurrLoc():

        # Use geopy to get lat and long

        lat = 0.0
        long = 0.0

        # City conversion still in progress !!!!!!!!!!!!!!!
        
        isValid = False

        while not isValid:
            useCurrLoc = input('Do you want to use your current location? (yes/no/cancel): ')
            if useCurrLoc.lower() == 'yes':
                loc = geocoder.ip('me')

                if loc.ok:
                    lat, long = loc.latlng
                    isValid = True
                else:
                    print("Could not retrieve current location")
            
            elif useCurrLoc.lower() == 'no':
                city = input("Enter City: ")
                loc = geocoder.osm(city)

                if loc.ok:
                    lat, long = loc.latlng
                    isValid = True
                else:
                    print("City could not be found. Try Again or choose your location.")
            elif useCurrLoc.lower() == 'cancel':
                raise Exception("Canceled")

        return lat, long


if __name__=="__main__":

    weather = Weather()

    lat, long = weather.SetCurrLoc()
    print(weather.ViewCurrWeather(lat, long))
    print(weather.ForecastHourly(lat, long))



