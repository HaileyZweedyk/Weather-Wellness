# This file will hold the running app
# Use Tkinter as the GUI plugin
import unittest
from WeatherCodeTranslations import WeatherCodeTranslations 
from Weather import Weather 
from Wellness import Clothing, Activities, Driving, Mood_Weather
import tkinter as tk
from tkinter import Label, Button
from PIL import Image, ImageTk

class Main:

    def __init__(self):
        pass


    def mainLoop(self):
        
        weather = Weather()
        lat, long = weather.SetCurrLoc()
        curr_weather = weather.ViewCurrWeather(lat, long)
        temp = curr_weather["CurrTemp"]

        currWeatherCode = curr_weather["CurrWeatherCode"]
        weatherTranslations = WeatherCodeTranslations()
        currWeatherText = weatherTranslations.GetConditions(currWeatherCode)
        
        root = tk.Tk()

        for row in range(10):
            for col in range(3):
                if row == 3:
                    label = tk.Label(root, padx=50, pady=0)
                    label.grid(row=row, column=col, padx=20, pady=5)
                elif row < 3:
                    label = tk.Label(root, padx=50, pady=5)
                    label.grid(row=row, column=col, padx=20, pady=0)
                else:
                    label = tk.Label(root, padx=50, pady=0)
                    label.grid(row=row, column=col, padx=20, pady=0)


        # Hourly Button
        hourly_button = Button(root, text="Hourly Forecast", width=10, height=2)
        hourly_button.grid(row=7, column=1, padx=5, pady=5)
        
        # Daily Button
        daily_button = Button(root, text="Daily Forecast", width=10, height=2)
        daily_button.grid(row=8, column=1, padx=5, pady=5)

        # Wellness Button
        wellness_button = Button(root, text="Wellness", width=10, height=2)
        wellness_button.grid(row=9, column=1, padx=5, pady=5)

        # Curr Weather
        # Location 
        strLat = str(lat)
        strLong = str(long)
        latlong = strLat + ", " + strLong
        location_label = Label(root, text=latlong, font=("Arial", 30))
        location_label.grid(row=0, column=1, padx=5, pady=5)

        image_path = "Images/sunIcon.png"  # Replace with your image path
        image = Image.open(image_path)
        image = image.resize((70, 70))  # Resize the image to fit
        weather_icon = ImageTk.PhotoImage(image)

        # Weather Icon
        weather_icon_label = tk.Label(root, image=weather_icon)
        weather_icon_label.grid(row=2, column=1, padx=5, pady=5)

        # Weather Text
        weather_text = Label(root, text=currWeatherText, font=("Arial", 18))
        weather_text.grid(row=3, column=1, padx=5, pady=5)

        # Temperature
        tempFull = str(int(temp)) + "\u00B0F"
        temp_label = Label(root, text=tempFull, font=("Arial", 25))
        temp_label.grid(row=1, column=1, padx=5, pady=5)

        # Run the Tkinter event loop
        root.mainloop()



    def hourlyForecast(self):
        pass


    def dailyForecast(self):
        pass


    def wellness(self):
        pass


if __name__ == "__main__":

    loop = Main()
    loop.mainLoop()