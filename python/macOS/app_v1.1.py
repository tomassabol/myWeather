from tkinter import *
from PIL import ImageTk, Image
from configparser import ConfigParser
import datetime
import requests
import geocoder
import json
import time


__author__ = "Tomas Sabol, https://github.com/tomassabol"


config_file = "config.ini"
config = ConfigParser()
config.read(config_file)
g = geocoder.ip('me') #get gps


# https://api.openweathermap.org/data/2.5/onecall?lat=1&lon=1&exclude=minutely,hourly&appid=|enter_your_api_key|&units=metric
url = f"https://api.openweathermap.org/data/2.5/onecall?lat={(g.lat)}&lon={(g.lng)}&exclude=minutely,hourly&appid=|enter_your_api_key|&units=metric"

response = requests.get(url) 
data = json.loads(response.text)


def getLocation():
    address = g.address
    location_label.config(text=address)


# functions
# get weather from url
def getWeather(): # get icon according to status
    current_temp = int(data["current"]["temp"])
    current_temp = str(current_temp) + "°C"
    temperature_label.config(text=current_temp)

    # update weather every minute
    temperature_label.after(60000, getWeather)
    root.update()


def getStatus():
    description = data["current"]["weather"]
    status = description[0]["description"].capitalize()
    status_label.config(text=status)


    if(int(time.ctime()[11]) == 0 and int(time.ctime()[12]) <= 6) or (int(time.ctime()[11:13]) >= 20):
        image_label.config(image=img2)
    else:
        # set icon based on status
        if status == "Clear sky":
            image_label.config(image=img7)
        elif status == "Scattered clouds" or status == "Broken clouds" or status == "Overcast clouds":
            image_label.config(image=img)
        elif status == "Rain" or status == "Shower rain":
            image_label.config(image=img4)
        elif status == "Snow" or status == "Light snow" or status == "Heavy snow":
            image_label.config(image=img5)
        elif status == "Thunderstorm":
            image_label.config(image=img6)
        elif status == "Few clouds":
            image_label.config(image=img3)


# get dates for next further forecast
def getDate():
      # load html
    weekDays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]  # day list

    day1 = datetime.date.today() + datetime.timedelta(days = 1)  # today's day + 1
    day1 = weekDays[day1.weekday()]  # get day name from ls
    day1_label.config(text=day1)

    day2 = datetime.date.today() + datetime.timedelta(days = 2)  # today's day + 2
    day2 = weekDays[day2.weekday()]  # get day name from ls
    day2_label.config(text=day2)

    day3 = datetime.date.today() + datetime.timedelta(days = 3)  # today's day + 3
    day3 = weekDays[day3.weekday()]  # get day name from ls
    day3_label.config(text=day3)

    day4 = datetime.date.today() + datetime.timedelta(days = 4)  # today's day + 4
    day4 = weekDays[day4.weekday()]  # get day name from ls
    day4_label.config(text=day4)


def getDailyWeather():
    day = data["daily"][0]
    day_1 = day["temp"]["day"]
    day_1 = str(int(day_1)) + "°C"
    temp1_label.config(text=day_1)

    day = data["daily"][1]
    day_2 = day["temp"]["day"]
    day_2 = str(int(day_2)) + "°C"
    temp2_label.config(text=day_2)

    day = data["daily"][2]
    day_3 = day["temp"]["day"]
    day_3 = str(int(day_3)) + "°C"
    temp3_label.config(text=day_3)

    day = data["daily"][3]
    day_4 = day["temp"]["day"]
    day_4 = str(int(day_4)) + "°C"
    temp4_label.config(text=day_4)


# window setup
# systemTransparent working on MAC OS X and later ONLY!!
# wait for windows specific app
root = Tk()
root.title("myWeather")
root.geometry("570x1212")
root.config(bg="systemTransparent")

# window ui
location_label = Label(root, text="", font=("SF Pro", 30, "bold"), bg="systemTransparent", fg="white")
location_label.pack(padx=70, pady = 60)

# load image + resize
img  = ImageTk.PhotoImage(Image.open("/Users/tomassabol/Documents/python/weatherApp/images/cloudy.png").resize((260,250)))
img2 = ImageTk.PhotoImage(Image.open("/Users/tomassabol/Documents/python/weatherApp/images/night.png").resize((260,250)))
img3 = ImageTk.PhotoImage(Image.open("/Users/tomassabol/Documents/python/weatherApp/images/partly-cloudy.png").resize((260,250)))
img4 = ImageTk.PhotoImage(Image.open("/Users/tomassabol/Documents/python/weatherApp/images/rain.png").resize((260,250)))
img5 = ImageTk.PhotoImage(Image.open("/Users/tomassabol/Documents/python/weatherApp/images/snow.png").resize((260,250)))
img6 = ImageTk.PhotoImage(Image.open("/Users/tomassabol/Documents/python/weatherApp/images/storm.png").resize((260,250)))
img7 = ImageTk.PhotoImage(Image.open("/Users/tomassabol/Documents/python/weatherApp/images/sun.png").resize((260,250)))

# output image
image_label = Label(root, bg="systemTransparent")
image_label.pack()

temperature_label = Label(root, text="", font=("SF Pro", 65, "bold"), bg="systemTransparent", fg="white")
temperature_label.pack(pady=10)

status_label = Label(root, text="", font=("SF Pro", 20, "bold"), bg="systemTransparent", fg="white")
status_label.pack(pady=10)


# frane to combine pack() && grid()
frame = Frame(root, bg = "black")


day1_label = Label(frame, bg = "black", fg="white", font=("SF Pro", 12,"bold"))
temp1_label = Label(frame, bg = "black", fg="white", font=("SF Pro", 10,"bold"))
day1_label.grid(row=0, column=0, padx=40)
temp1_label.grid(row=1, column=0, padx=40)

day2_label = Label(frame, bg = "black", fg="white", font=("SF Pro", 12,"bold"))
temp2_label = Label(frame, bg = "black", fg="white", font=("SF Pro", 10,"bold"))
day2_label.grid(row=0, column=1, padx=40)
temp2_label.grid(row=1, column=1, padx=40)

day3_label = Label(frame, bg = "black", fg="white", font=("SF Pro", 12,"bold"))
temp3_label = Label(frame, bg = "black", fg="white", font=("SF Pro",10, "bold"))
day3_label.grid(row=0, column=2, padx=40)
temp3_label.grid(row=1, column=2, padx=40)

day4_label = Label(frame, bg = "black", fg="white", font=("SF Pro", 12,"bold"))
temp4_label = Label(frame, bg = "black", fg="white", font=("SF Pro", 10,"bold"))
day4_label.grid(row=0, column=3, padx=40)
temp4_label.grid(row=1, column=3, padx=40)


frame.pack(pady=100)


def main():
    getWeather()
    getStatus()
    getDate()
    getLocation()
    getDailyWeather()
    root.mainloop()

if __name__ == "__main__":
    main()
