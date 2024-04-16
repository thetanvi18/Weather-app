
import requests
import datetime
import tkinter as tk
from tkinter import ttk

api_keys = {
    "default": "e36f038aa5e6ecac47098218895399b4",
    "location1": "API_KEY_FOR_LOCATION_1",
    "location2": "API_KEY_FOR_LOCATION_2",
}

city_name_mapping = {
    "Prayagraj": "Allahabad",
}

def get_location():
    return "default"

def get_weather(city):
    api_key = api_keys[get_location()]
    
    if city in city_name_mapping:
        city = city_name_mapping[city]
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data["cod"] == 200:
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        wind_speed = data["wind"]["speed"] * 3.6
        dt = datetime.datetime.now()
        return weather_description, temperature, feels_like, wind_speed, dt
    else:
        return None, None, None, None, None

def display_weather():
    city = city_entry.get()
    weather_details = get_weather(city)
    if weather_details is not None:
        weather_description, temperature, feels_like, wind_speed, dt = weather_details
        city_label.config(text=f"City: {city}")
        date_time_label.config(text=f"Date & Time: {dt.strftime('%Y-%m-%d %H:%M:%S')}")
        weather_label.config(text=f"Weather: {weather_description}")
        temp_label.config(text=f"Temperature: {temperature}°C")
        feels_like_label.config(text=f"Feels Like: {feels_like}°C")
        wind_speed_label.config(text=f"Wind Speed: {wind_speed:.1f} km/h")

def clear_entry(event):
    if city_entry.get() == "Enter name:":
        city_entry.delete(0, 'end')

root = tk.Tk()

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

style = ttk.Style()

style.configure("Custom.TLabel", background="#f0f0f0", foreground="black")

style.configure("Custom.TLabel", font=("Times New Roman", 18))

city_label = ttk.Label(root, text="City:", style="Custom.TLabel")
city_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

city_entry = ttk.Entry(root, width=20)
city_entry.insert(0, "Enter name:")
city_entry.bind("<Button-1>", clear_entry)
city_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

display_button = ttk.Button(root, text="Display Weather", command=display_weather)
display_button.grid(row=0, column=2, padx=10, pady=10, sticky="w")

weather_label = ttk.Label(root, text="", style="Custom.TLabel")
weather_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="w")

date_time_label = ttk.Label(root, text="", style="Custom.TLabel")
date_time_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="w")

temp_label = ttk.Label(root, text="", style="Custom.TLabel")
temp_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")

feels_like_label = ttk.Label(root, text="", style="Custom.TLabel")
feels_like_label.grid(row=3, column=1, padx=10, pady=10, sticky="w")

wind_speed_label = ttk.Label(root, text="", style="Custom.TLabel")
wind_speed_label.grid(row=3, column=2, padx=10, pady=10, sticky="w")

root.mainloop()
