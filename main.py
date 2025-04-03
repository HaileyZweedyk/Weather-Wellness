# This file will hold the running app
# Use Tkinter as the GUI plugin

import tkinter as tk
from tkinter import Label, Button
from PIL import Image, ImageTk

# Create the main window
root = tk.Tk()
root.title("Weather App Grid")

# Configure grid weights so it expands properly
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Back button at (1,1)
back_button = Button(root, text="Back", width=10, height=2)
back_button.grid(row=1, column=1, padx=5, pady=5)

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