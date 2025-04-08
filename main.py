# This file will hold the running app
# Use Tkinter as the GUI plugin
import unittest
from WeatherCodeTranslations import WeatherCodeTranslations 
from Weather import Weather 
from Wellness import Clothing, Activities, Driving, Mood_Weather, Mood_Forecast
import tkinter as tk
from tkinter import Label, Button
from PIL import Image, ImageTk

if __name__ == "__main__":

    root = tk.Tk()
    root.geometry("400x500")  # Set window size to 400x300
    root.resizable(False, False)

    for i in range(5):
        root.grid_columnconfigure(i, weight=1)

    # Hourly Button
    hourly_button = Button(root, text="Hourly Forecast", width=10, height=2)
    hourly_button.grid(row=2, column=1, padx=5, pady=5)
    
    # Daily Button
    daily_button = Button(root, text="Daily Forecast", width=10, height=2)
    daily_button.grid(row=1, column=1, padx=5, pady=5)

    # Wellness Button
    wellness_button = Button(root, text="Wellness", width=10, height=2)
    wellness_button.grid(row=3, column=1, padx=5, pady=5)

    # Curr Weather
    # Location label at (1,2)
    location_label = Label(root, text="Location", font=("Arial", 12, "bold"))
    location_label.grid(row=1, column=2, padx=5, pady=5)

    image_path = "Images/sunIcon.png"  # Replace with your image path
    image = Image.open(image_path)
    image = image.resize((50, 50))  # Resize the image to fit
    weather_icon = ImageTk.PhotoImage(image)

    # Placeholder for weather icon at (2,2)
    weather_icon_label = tk.Label(root, image=weather_icon)
    weather_icon_label.grid(row=2, column=2, padx=5, pady=5)

    # Weather text at (3,2)
    weather_text = Label(root, text="Sunny", font=("Arial", 12))
    weather_text.grid(row=3, column=2, padx=5, pady=5)

    # Run the Tkinter event loop
    root.mainloop()



def hourlyForecast():
    pass


def dailyForecast():
    pass


def wellness():