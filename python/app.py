# IMPORTANT
# read README before running the code!
import requests
from tkinter import *
from PIL import ImageTk, Image
from bs4 import BeautifulSoup
import datetime
import time

__author__ = "Tomas Sabol, https://github.com/tomassabol"

# url
url = "https://weather.com/weather/today/l/6b4e03876dab102b4e87b32fc3946e9bf64800e6bc1606968f95d33620c67c8a"
page = requests.get(url) # load page /url


# funcitons
# get weather from url
def getWeather():
    # load page htmk
    soup = BeautifulSoup(page.content, "html.parser")
    
    # get data from html elements
    location = soup.find("h1",class_="CurrentConditions--location--1Ayv3").text  # load location from element
    location_label.config(text=location[:-7]) # pull location name without word "weather"

    temperature = soup.find("span",class_="CurrentConditions--tempValue--3KcTQ").text  # load temp
    temperature_label.config(text=temperature)
    unitCheck()

    weatherPrediction = soup.find("div", class_="CurrentConditions--phraseValue--2xXSr").text  # load weather status
    weather_prediction_label.config(text=weatherPrediction)
    getIcon()  # get icon according to status


    temperature_label.after(60000, getWeather)  # update weather every minute
    root.update()


# get dates for next further forecast
def getDate():
    soup = BeautifulSoup(page.content, "html.parser")  # load html
    weekDays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]  # day list


    day1 = datetime.date.today() + datetime.timedelta(days = 1)  # today's day + 1
    day1 = weekDays[day1.weekday()]  # get day name from ls
    day1_label.configure(text=day1)

    day2 = datetime.date.today() + datetime.timedelta(days = 2)  # today's day + 2
    day2 = weekDays[day2.weekday()]  # get day name from ls
    day2_label.configure(text=day2)

    day3 = datetime.date.today() + datetime.timedelta(days = 3)  # today's day + 3
    day3 = weekDays[day3.weekday()]  # get day name from ls
    day3_label.configure(text=day3)

    day4 = datetime.date.today() + datetime.timedelta(days = 4)  # today's day + 4
    day4 = weekDays[day4.weekday()]  # get day name from ls
    day4_label.configure(text=day4)

    # I was unable to get specific temp forecast for each day, as they use the same class
    # will try to find solution for the v1.1

    temp1 = soup.find("div",class_="Column--temp--2v_go").text
    temp1_label.configure(text=temp1)

    temp2 = soup.find("div",class_="Column--temp--2v_go").text
    temp2_label.configure(text=temp1)

    temp3 = soup.find("div",class_="Column--temp--2v_go").text
    temp3_label.configure(text=temp1)

    temp4 = soup.find("div",class_="Column--temp--2v_go").text
    temp4_label.configure(text=temp1)


# check for default temp unit
def unitCheck():
    soup = BeautifulSoup(page.content, "html.parser")  # load html
    unit = soup.find("span", class_="LanguageSelector--unitDisplay--eg0E7").text  # get data frim span element
    #  check for specific unit
    # if set to F, do F3C func, else continue
    if unit == "°F":
        F2C()
    else:
        pass
    

# convert f to c
def F2C():
    soup = BeautifulSoup(page.content, "html.parser")  # load html
    temperature = int(soup.find("span", class_="CurrentConditions--tempValue--3KcTQ").text[:-1]) # get span element data and remove "°"
    result = str(round((temperature - 32) / 1.8))  # F2C formula + convert to string for output
    temperature_label.config(text=result + "°C")


# get icon based on weather status
def getIcon():
    soup = BeautifulSoup(page.content, "html.parser")  # load html
    status = str(soup.find("div", class_="CurrentConditions--phraseValue--2xXSr").text)  # get div elemtnt data

    # set icon based on condition
    if status == "Clear" and (time.ctime()[-13:-11] == "21","22","23","00","01","02","03","04","05"):
        image.config(image=img2)
    elif status == "Sunny" or status == "Clear":
        image.config(image=img7)
    elif status == "Partly Cloudy":
        image.config(image=img3)
    elif status == "Cloudy":
        image.config(image=img)
    elif status == "Rain/Snow Showers" or "Rain" or "PM Showers" or "AM Showers" or "Showers":
        image.config(image=img4)
    elif status == "Snow" or "PM Snow Showers" or "AM Snow Showers" or "Snow Showers":
        image.config(image=img5)
    elif status == "Storm":
        image.config(image=img6)


# window setup
# systemTransparent working on MAC OS X and later ONLY!!
# wait for windows specific app
root = Tk()
root.title("myWeather")
root.geometry("570x1212")
root.configure(bg="systemTransparent")

# window ui
location_label = Label(root, text="location", font=("SF Pro", 30, "bold"), bg="systemTransparent", fg="white")
location_label.pack(padx=70, pady = 60)

# load image + resize
img = ImageTk.PhotoImage(Image.open("/Users/tomassabol/Documents/python/weatherApp/cloudy.png").resize((260,250)))
img2 = ImageTk.PhotoImage(Image.open("/Users/tomassabol/Documents/python/weatherApp/night.png").resize((260,250)))
img3 = ImageTk.PhotoImage(Image.open("/Users/tomassabol/Documents/python/weatherApp/partly-cloudy.png").resize((260,250)))
img4 = ImageTk.PhotoImage(Image.open("/Users/tomassabol/Documents/python/weatherApp/rain.png").resize((260,250)))
img5 = ImageTk.PhotoImage(Image.open("/Users/tomassabol/Documents/python/weatherApp/snow.png").resize((260,250)))
img6 = ImageTk.PhotoImage(Image.open("/Users/tomassabol/Documents/python/weatherApp/storm.png").resize((260,250)))
img7 = ImageTk.PhotoImage(Image.open("/Users/tomassabol/Documents/python/weatherApp/sun.png").resize((260,250)))

# output image
image = Label(root, image=img, bg="systemTransparent")
image.pack()

temperature_label = Label(root, text="temperature", font=("SF Pro", 65, "bold"), bg="systemTransparent", fg="white")
temperature_label.pack(pady=10)

weather_prediction_label = Label(root, text="temperature", font=("SF Pro", 20, "bold"), bg="systemTransparent", fg="white")
weather_prediction_label.pack(pady=10)


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

while True:
    getWeather()
    getDate()

root.mainloop()
