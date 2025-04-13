# pip install geopy certifi pillow

from WeatherCodeTranslations import WeatherCodeTranslations 
from Weather import Weather 
from Wellness import Clothing, Activities, Driving, Mood_Weather

# GUI
import tkinter as tk
from tkinter import Label, Button
from PIL import Image, ImageTk

# Local Time
from datetime import datetime

# Get Location
import ssl
import certifi
from geopy.geocoders import Nominatim
import geopy.geocoders

class Main:

    def __init__(self):
        self.root = ""
        self.now = datetime.now()
        self.currentTime = self.now.strftime("%H:%M")
        self.weatherIcons = []
        self.days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        self.city = ""


# This is the inital page of the app when you first launch
# This shows the current weather and also holds the hourly daily and wellness access buttons
    def mainLoop(self):

        weather = Weather()
        lat, long = weather.SetCurrLoc()
        
        # Variable Declarations
        curr_weather = weather.ViewCurrWeather(lat, long)
        temp = curr_weather["CurrTemp"]

        currWeatherCode = curr_weather["CurrWeatherCode"]
        isDay = curr_weather["CurrIsDay"]
        weatherTranslations = WeatherCodeTranslations()
        currWeatherText = weatherTranslations.GetConditions(currWeatherCode)
        currWeatherCat = weatherTranslations.GetCategory(currWeatherCode, isDay)
        if isDay and currWeatherText == "Clear":
                currWeatherText = "Sunny"

        # If there is a current self.root, then destroy, if not, ignore
        if self.root != "":
            self.root.destroy()
        
        # Creates window for main loop
        self.root = tk.Tk()
        self.root.title("Current Condtions")

        # Creates 11x3 grid
        for row in range(11):
            for col in range(3):
                if row == 3:
                    label = tk.Label(self.root, padx=50, pady=0)
                    label.grid(row=row, column=col, padx=20, pady=5)
                elif row < 3:
                    label = tk.Label(self.root, padx=50, pady=5)
                    label.grid(row=row, column=col, padx=20, pady=0)
                else:
                    label = tk.Label(self.root, padx=50, pady=0)
                    label.grid(row=row, column=col, padx=20, pady=0)

        # Get Nearest City/Location
        self.getNearestCity(lat, long)
        location_label = Label(self.root, text=self.city, font=("Arial", 30))
        location_label.grid(row=0, column=1, padx=5, pady=5)

        # Check Weather
        imageName = self.checkWeatherCat(currWeatherCat)

        # Image
        image_path = imageName
        image = Image.open(image_path).convert("RGBA")
        image = image.resize((200, 200))
        weather_icon = ImageTk.PhotoImage(image)

        self.weatherIcons.append(weather_icon)  # prevent GC

        # Weather Icon Grid
        weather_icon_label = tk.Label(self.root, image=weather_icon)
        weather_icon_label.grid(row=2, column=1, padx=5, pady=5)

        # Weather Text
        weather_text = Label(self.root, text=currWeatherText, font=("Arial", 28))
        weather_text.grid(row=3, column=1, padx=5, pady=5)

        # Temperature
        tempFull = str(int(temp)) + "\u00B0F"
        temp_label = Label(self.root, text=tempFull, font=("Arial", 25))
        temp_label.grid(row=1, column=1, padx=5, pady=5)

        # Hourly Button
        hourly_button = Button(self.root, text="Hourly Forecast", width=10, height=2, command=self.hourlyForecast)
        hourly_button.grid(row=7, column=1, padx=5, pady=5)
        
        # Daily Button
        daily_button = Button(self.root, text="Daily Forecast", width=10, height=2, command=self.dailyForecast)
        daily_button.grid(row=8, column=1, padx=5, pady=5)

        # Wellness Button
        wellness_button = Button(self.root, text="Wellness", width=10, height=2, command=self.wellness)
        wellness_button.grid(row=9, column=1, padx=5, pady=5)

        # Time Label
        temp_icon_label = tk.Label(self.root, text=self.currentTime, font=("Arial", 15))
        temp_icon_label.grid(row=10, column=1, padx=5, pady=5)
        

        # Run the Tkinter event loop
        self.root.mainloop()



# Function that runs upon the click of the hourly button
# Shows a list of the forecast for the next 24 hours from the current hour
    def hourlyForecast(self):

        # Variable Declaration
        weather = Weather()
        lat, long = weather.SetCurrLoc()
        hourlyDict = weather.ForecastHourly(lat, long)
        hourlyTempArr = hourlyDict["HourlyTemp"]
        hourlyWeatherCodeArr = hourlyDict["HourlyWeatherCode"]
        hourlyWindSpeedArr = hourlyDict["HourlyWindSpeed"]
        hourlyWindDirArr = hourlyDict["HourlyWindDir"]

        isDay = False
        now = datetime.now()
        hour = int(now.hour)
        hourNew = hour
        timeStr = str(hourNew) + ":00"

        # Gets rid of the current window
        self.root.destroy()

        # Creates the new window
        self.root = tk.Tk()
        self.root.title("Hourly Forecast")

        # Back Button
        back_button = Button(self.root, text="Back", width=10, height=2, command=self.mainLoop)
        back_button.grid(row=0, column=0, padx=5, pady=0)

        # Conditions Label
        tk.Label(self.root, text="Conditions", font=("Times New Roman", 26)).grid(row=1, column=1, padx=20, pady=10)

        # Temperature Label
        tk.Label(self.root, text="Temperature", font=("Times New Roman", 26)).grid(row=1, column=2, padx=20, pady=10)

        # Wind Speed Label
        tk.Label(self.root, text="Wind Speed", font=("Times New Roman", 26)).grid(row=1, column=3, padx=20, pady=10)

        # Wind Direction Label
        tk.Label(self.root, text="Wind Direction", font=("Times New Roman", 26)).grid(row=1, column=4, padx=20, pady=10)

        # Local Time 24h Label
        tk.Label(self.root, text="Local Time 24h", font=("Times New Roman", 26)).grid(row=1, column=5, padx=20, pady=10)


        # Iterators for for loop
        i = hour
        count = 2

        # This loop iterates through the 48 hour list (starting from 0:00 each day) of each hours forecast from the current hour, only displays 24 hours to the next instance of the current hour the next day
        for i in range(i, i + 25):

            # Individual Hour Variable Declarations
            hourlyWeatherCode = hourlyWeatherCodeArr[i]
            hourlyTemp = int(hourlyTempArr[i])
            hourlyTempStr = str(hourlyTemp) + "\u00B0F"
            hourlyWindSpeed = int(hourlyWindSpeedArr[i])
            hourlyWindDir = int(hourlyWindDirArr[i])
            hourlyWindDirStr = self.getWindDir(hourlyWindDir)
            hourlyWindSpeedStr = str(hourlyWindSpeed) + " mph"

        
            # If its between the hours of 8am and 8pm, isDay will be false meaning it's night
            if 8 <= hourNew <= 20:
                isDay = True

            weatherTranslations = WeatherCodeTranslations()
            hourlyWeatherText = weatherTranslations.GetConditions(hourlyWeatherCode)
            hourlyWeatherCat = weatherTranslations.GetCategory(hourlyWeatherCode, isDay)
            if isDay and hourlyWeatherText == "Clear":
                hourlyWeatherText = "Sunny"
            if hourlyWeatherText == "Conditions Remain Same":
                hourlyWeatherText = weatherTranslations.GetConditions(hourlyWeatherCodeArr[i-1])
                hourlyWeatherCat = weatherTranslations.GetCategory(hourlyWeatherCodeArr[i-1], isDay)

            # Check Weather
            imageName = self.checkWeatherCat(hourlyWeatherCat)

            image = Image.open(imageName).convert("RGBA")
            img = image.resize((30, 30)) 
            weather_icon = ImageTk.PhotoImage(img)

            self.weatherIcons.append(weather_icon)  # prevent GC

            # Weather Icon Grid
            weather_icon_label = tk.Label(self.root, image=weather_icon)
            weather_icon_label.grid(row=count, column=0, padx=5, pady=2)


            # Weather Text
            tk.Label(self.root, text=hourlyWeatherText, font=("Times New Roman", 20)).grid(row=count, column=1, padx=35, pady=2)

            # Temperature
            tk.Label(self.root, text=hourlyTempStr, font=("Times New Roman", 18)).grid(row=count, column=2, padx=25, pady=2)

            # Wind Speed
            tk.Label(self.root, text=hourlyWindSpeedStr, font=("Times New Roman", 16)).grid(row=count, column=3, padx=25, pady=2)

            # Wind Direction
            tk.Label(self.root, text=hourlyWindDirStr, font=("Times New Roman", 16)).grid(row=count, column=4, padx=10, pady=2)

            # Time
            tk.Label(self.root, text=timeStr, font=("Times New Roman", 16)).grid(row=count, column=5, padx=20, pady=2)

            # Iterates the row number
            count += 1

            # If its currently 23:00 (11pm) the hour will be reset to 0:00 (12am)
            if hourNew < 23:
                hourNew += 1
                timeStr = str(hourNew) + ":00"
            else:
                hourNew = 0
                timeStr = str(hourNew) + ":00"

        # Project name label on bottom
        tk.Label(self.root, text="Weather Wellness", font=("Arial", 8)).grid(row=28, column=5, padx=20, pady=10)


        self.root.mainloop()

        

# Function that runs upon the click of the daily button
# Shows a list of the forecast for the next 7 days
    def dailyForecast(self):

        # Variable Declaration
        weather = Weather()
        lat, long = weather.SetCurrLoc()
        dailyDict = weather.ForecastDaily(lat, long)
        dailyTempMaxArr = dailyDict["DailyTempMax"]
        dailyTempMinArr = dailyDict["DailyTempMin"]
        dailyWeatherCodeArr = dailyDict["DailyWeatherCode"]
        dailyWindSpeedArr = dailyDict["DailyWindSpeed"]
        isDay = True
        

        # Destroy Current Window
        self.root.destroy()

        # Create New Window
        self.root = tk.Tk()
        self.root.title("Daily Forecast")

        # Back Button
        back_button = Button(self.root, text="Back", width=10, height=2, command=self.mainLoop)
        back_button.grid(row=0, column=0, padx=5, pady=0)

        # Pulls current day in text format i.e "Monday"
        currDay = self.now.strftime("%A")
        dayStr = currDay

        # Finds the current days index in the self.days array
        currDayIndex = self.days.index(currDay)

        # This for loop iterates over all 7 days to display the forecasting data
        for i in range(7):

            # Set start of days; if the end of the week (saturday) is the current day, it will iterate to the start of the list (sunday)
            tk.Label(self.root, text=dayStr, font=("Times New Roman", 30)).grid(row=1, column=i, padx=20, pady=50)
            if currDayIndex < 6:
                currDayIndex += 1
                dayStr = self.days[currDayIndex]
            else:
                currDayIndex = 0
                dayStr = self.days[currDayIndex]

            # Variable Declarations
            dailyWeatherCode = dailyWeatherCodeArr[i]
            dailyTempMax = int(dailyTempMaxArr[i])
            dailyTempMaxStr = str(dailyTempMax) + "\u00B0F"
            dailyTempMin = int(dailyTempMinArr[i])
            dailyTempMinStr = str(dailyTempMin) + "\u00B0F"
            dailyWindSpeed = int(dailyWindSpeedArr[i])
            dailyWindSpeedStr = str(dailyWindSpeed) + " mph"

            weatherTranslations = WeatherCodeTranslations()
            dailyWeatherText = weatherTranslations.GetConditions(dailyWeatherCode)
            dailyWeatherCat = weatherTranslations.GetCategory(dailyWeatherCode, isDay)
            if isDay and dailyWeatherText == "Clear":
                dailyWeatherText = "Sunny"


            # Check Weather
            imageName = self.checkWeatherCat(dailyWeatherCat)

            # Image
            image_path = imageName
            image = Image.open(image_path).convert("RGBA")
            image = image.resize((100, 100))
            weather_icon = ImageTk.PhotoImage(image)

            self.weatherIcons.append(weather_icon)  # prevent GC

            # Weather Icon Grid
            weather_icon_label = tk.Label(self.root, image=weather_icon)
            weather_icon_label.grid(row=2, column=i, padx=20, pady=15)

            # Weather Text
            weather_text = Label(self.root, text=dailyWeatherText, font=("Times New Roman", 26))
            weather_text.grid(row=3, column=i, padx=20, pady=15)

            # Temperature
            tempMax_label = Label(self.root, text=dailyTempMaxStr, font=("Times New Roman", 23))
            tempMax_label.grid(row=4, column=i, padx=20, pady=15)

            tempMin_label = Label(self.root, text=dailyTempMinStr, font=("Times New Roman", 19))
            tempMin_label.grid(row=5, column=i, padx=20, pady=0)

            # Wind Speed
            tk.Label(self.root, text=dailyWindSpeedStr, font=("Times New Roman", 16)).grid(row=6, column=i, padx=20, pady=10)

        # Project name label on bottom
        tk.Label(self.root, text="Weather Wellness", font=("Arial", 8)).grid(row=29, column=6, padx=20, pady=10)

        self.root.mainloop()



# This is the function that brings you to the wellness section upon click of the wellness button
# This shows predicive moods and allows you to journal how you feel
    def wellness(self):

        # Destroy Current Window
        self.root.destroy()

        # Create New Window
        self.root = tk.Tk()
        self.root.title("Wellness")


    def getWindDir(self, windDir):

        hourlyWindDirStr = ""

        if 10 < windDir and windDir > 350:
            hourlyWindDirStr = "N"
        elif 10 <= windDir <= 80:
            hourlyWindDirStr = "NE"
        elif 80 < windDir < 100:
            hourlyWindDirStr = "E"
        elif 100 <= windDir <= 170:
            hourlyWindDirStr = "SE"
        elif 170 < windDir < 190:
            hourlyWindDirStr = "S"
        elif 190 <= windDir <= 260:
            hourlyWindDirStr = "SW"
        elif 260 < windDir < 280:
            hourlyWindDirStr = "W"
        elif 280 <= windDir <= 350:
            hourlyWindDirStr = "NW"
        
        return hourlyWindDirStr

    def checkWeatherCat(self, weatherCat):

        if weatherCat == "Sunny":
            return "Images/sunIcon.png"
        elif weatherCat == "Clear":
            return "Images/moonIcon.png"
        elif weatherCat == "Cloudy":
            return "Images/cloudyIcon.png"
        elif weatherCat == "Partly Cloudy":
            return "Images/partlyCloudyIcon.png"
        elif weatherCat == "Partly Cloudy Night":
            return "Images/partlyCloudyNightIcon.png"
        elif weatherCat == "Rain":
            return "Images/rainIcon.png"
        elif weatherCat == "Thunderstorm":
            return "Images/thunderstormIcon.png"
        elif weatherCat == "Snow":
            return "Images/snowIcon.png"
        elif weatherCat == "Haze":
            return "Images/hazeIcon.png"
        elif weatherCat == "Wintery Mix":
            return "Images/winteryMixIcon.png"
        elif weatherCat == "Fog":
            return "Images/fogIcon.png"
        else:
            return "Images/errorIcon.png"
        

    def getNearestCity(self, lat, long):
        geopy.geocoders.options.default_ssl_context = ssl.create_default_context(cafile=certifi.where())

        geolocator = Nominatim(user_agent="Weather_Wellness_hazweedyk@gmail.com")

        # Reverse geocoding
        location = geolocator.reverse((lat, long), exactly_one=True)

        # Get city name
        if location:
            address = location.raw['address']
            self.city = address.get('city', '') or address.get("town") or address.get("village") or address.get("hamlet") or address.get("county")
        else:
            print("Location not found.")

        

if __name__ == "__main__":

    loop = Main()
    loop.mainLoop()