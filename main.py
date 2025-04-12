from WeatherCodeTranslations import WeatherCodeTranslations 
from Weather import Weather 
from Wellness import Clothing, Activities, Driving, Mood_Weather

# GUI
import tkinter as tk
from tkinter import Label, Button
from PIL import Image, ImageTk

# Local Time
from datetime import datetime

class Main:

    def __init__(self):
        self.root = ""
        self.now = datetime.now()
        self.currentTime = self.now.strftime("%H:%M:%S")
        self.weatherIcons = []

    def mainLoop(self):
        
        weather = Weather()
        lat, long = weather.SetCurrLoc()
        curr_weather = weather.ViewCurrWeather(lat, long)
        temp = curr_weather["CurrTemp"]

        currWeatherCode = curr_weather["CurrWeatherCode"]
        isDay = curr_weather["CurrIsDay"]
        weatherTranslations = WeatherCodeTranslations()
        currWeatherText = weatherTranslations.GetConditions(currWeatherCode)
        currWeatherCat = weatherTranslations.GetCategory(currWeatherCode, isDay)

        
        if self.root != "":
            self.root.destroy()
        
        
        self.root = tk.Tk()

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

        # Curr Weather
        # Location 
        strLat = str(lat)
        strLong = str(long)
        latlong = strLat + ", " + strLong
        location_label = Label(self.root, text=latlong, font=("Arial", 30))
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

        # Run the Tkinter event loop
        self.root.mainloop()


    def checkWeatherCat(self, weatherCat):

        if weatherCat == "Sunny":
            return "Images/sunIcon.png"
        elif weatherCat == "Clear":
            return "Images/moonIcon.png"
        elif weatherCat == "Cloudy":
            return "Images/cloudyIcon.png"
        elif weatherCat == "Partly Cloudy":
            return "Images/partlyCloudyIcon.png"
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
            return "Images/sunIcon.png"


    def hourlyForecast(self):

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
        adjustedTime = 0
        adjustedTimeStr = str(adjustedTime) + ":00"

        self.root.destroy()

        self.root = tk.Tk()

        

        for i in range(0, 26):

            if i == 0:
                # Back Button
                back_button = Button(self.root, text="Back", width=10, height=2, command=self.mainLoop)
                back_button.grid(row=0, column=0, padx=5, pady=5)
            else:

                hourlyWeatherCode = hourlyWeatherCodeArr[i]
                hourlyTemp = int(hourlyTempArr[i])
                hourlyTempStr = str(hourlyTemp) + "\u00B0F"
                hourlyWindSpeed = int(hourlyWindSpeedArr[i])
                hourlyWindDir = int(hourlyWindDirArr[i])

                # If its between the hours of 8am and 8pm, isDay will be false meaning it's night
                if 8 <= adjustedTime <= 20:
                    isDay = True

                weatherTranslations = WeatherCodeTranslations()
                hourlyWeatherText = weatherTranslations.GetConditions(hourlyWeatherCode)
                hourlyWeatherCat = weatherTranslations.GetCategory(hourlyWeatherCode, isDay)

                # Check Weather
                imageName = self.checkWeatherCat(hourlyWeatherCat)

                image = Image.open(imageName).convert("RGBA")
                img = image.resize((30, 30)) 
                weather_icon = ImageTk.PhotoImage(img)

                self.weatherIcons.append(weather_icon)  # prevent GC

                # Weather Icon Grid
                weather_icon_label = tk.Label(self.root, image=weather_icon)
                weather_icon_label.grid(row=i, column=0, padx=5, pady=2)


                # Add text labels at (1,1), (1,2), (1,3)
                tk.Label(self.root, text=hourlyWeatherText, font=("Arial", 20)).grid(row=i, column=1, padx=35, pady=2)
                tk.Label(self.root, text=hourlyTempStr, font=("Arial", 12)).grid(row=i, column=2, padx=25, pady=2)
                tk.Label(self.root, text=hourlyWindSpeed, font=("Arial", 12)).grid(row=i, column=3, padx=25, pady=2)
                tk.Label(self.root, text=hourlyWindDir, font=("Arial", 12)).grid(row=i, column=4, padx=10, pady=2)
                tk.Label(self.root, text=adjustedTimeStr, font=("Arial", 12)).grid(row=i, column=5, padx=20, pady=2)

                adjustedTime += 1
                adjustedTimeStr = str(adjustedTime) + ":00"

        self.root.mainloop()

        


    def dailyForecast(self):
        pass


    def wellness(self):
        pass


if __name__ == "__main__":

    loop = Main()
    loop.mainLoop()