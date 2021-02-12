from tkinter import *
from PIL import ImageTk,Image
from configparser import ConfigParser
import requests

url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

config_file = "config.ini"
config = ConfigParser()
config.read(config_file)
api_key = config["api_key"]["key"]

# functions

def get_weather():
    result = requests.get(url.format(city, api_key))
    if result:
         json = result.json()
         city = json["name"]
         country = json["sys"]["country"]
         temp_kelvin
    else:
        return None


get_weather("London")


def search():
    pass


# window setup
root=Tk()
root.title("myWeather")
root.geometry("570x1212")


#  ui
city_text = StringVar
city_text = Entry(root, textvariable=city_text)
city_text.pack()

search_btn = Button(root, text="Search", width=10, command=search)
search_btn.pack()

location_label = Label(root, text="Location", font=("SF Pro", 40, "bold"))
location_label.pack()

image_label = Label(root)
image_label.pack()

temperature_label = Label(root, text="temperature", font=("SF Pro", 12, "bold"))
temperature_label.pack()

weather_label = Label(root, text="weather", font=("SF Pro", 12, "bold"))
weather_label.pack()


root.mainloop()
