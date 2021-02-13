import requests
from tkinter import *
from PIL import ImageTk, Image
from bs4 import BeautifulSoup
import datetime
import time

# url
url = "https://weather.com/weather/today/l/6b4e03876dab102b4e87b32fc3946e9bf64800e6bc1606968f95d33620c67c8a"
page = requests.get(url) # load page /url


# funcitons
# get weather from url
def getWeather():
    # load page
    soup = BeautifulSoup(page.content, "html.parser")
    
    # get data from elements
    location = soup.find("h1",class_="CurrentConditions--location--1Ayv3").text  # load location from element
    location_label.config(text=location[:-7])

    temperature = soup.find("span",class_="CurrentConditions--tempValue--3KcTQ").text  # load temp
    temperature_label.config(text=temperature)

    weatherPrediction = soup.find("div", class_="CurrentConditions--phraseValue--2xXSr").text  # load weather status
    weather_prediction_label.config(text=weatherPrediction)
    unitCheck()
    getIcon()


    temperature_label.after(60000, getWeather)
    root.update()


# get day for next further forecast
def getDate():
    soup = BeautifulSoup(page.content, "html.parser")
    weekDays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]


    day1 = datetime.date.today() + datetime.timedelta(days = 1)
    day1 = weekDays[day1.weekday()]
    day1_label.configure(text=day1)

    day2 = datetime.date.today() + datetime.timedelta(days = 2)
    day2 = weekDays[day2.weekday()]
    day2_label.configure(text=day2)

    day3 = datetime.date.today() + datetime.timedelta(days = 3)
    day3 = weekDays[day3.weekday()]
    day3_label.configure(text=day3)

    day4 = datetime.date.today() + datetime.timedelta(days = 4)
    day4 = weekDays[day4.weekday()]
    day4_label.configure(text=day4)


    temp1 = soup.find("div",class_="Column--temp--2v_go").text
    temp1_label.configure(text=temp1)

    temp2 = soup.find("div",class_="Column--temp--2v_go").text
    temp2_label.configure(text=temp1)

    temp3 = soup.find("div",class_="Column--temp--2v_go").text
    temp3_label.configure(text=temp1)

    temp4 = soup.find("div",class_="Column--temp--2v_go").text
    temp4_label.configure(text=temp1)



def unitCheck():
    soup = BeautifulSoup(page.content, "html.parser")
    unit = soup.find("span", class_="LanguageSelector--unitDisplay--eg0E7").text
    
    if unit == "°F":
        F2C()
    else:
        pass


def F2C():
    soup = BeautifulSoup(page.content, "html.parser")
    temperature = int(soup.find("span", class_="CurrentConditions--tempValue--3KcTQ").text[:-1])
    result = str(round((temperature - 32) / 1.8,1)) 
    temperature_label.config(text=result + "°C")


def getIcon():
    soup = BeautifulSoup(page.content, "html.parser")
    status = soup.find("div", class_="CurrentConditions--phraseValue--2xXSr").text

    
    if status == "Clear" and (time.ctime()[-13:-11] == "21","22","23","00","01","02","03","04","05"):
        image.config(image=img2)
    elif status == "Clear":
        image.config(image=img7)
    elif status == "Partly Cloudy" or "Mostly Clear":
        image.config(image=img3)
    elif status == "Cloudy":
        image.config(image=img)
    elif status == "Rain/Snow Showers" or "Rain" or "PM Showers" or "AM Showers" or "Showers":
        image.config(image=img4)
    elif status == "Snow" or "PM Snow Showers" or "AM Snow Showers" or "Snow Showers":
        image.config(image=img5)
    elif status == "Storm":
        image.config(image=img6)
    elif status == "Sunny":
        image.config(image=img7)


# window setup
root = Tk()
root.title("myWeather")
root.geometry("570x1212")
root.configure(bg="#2a2a2a")

# window ui
location_label = Label(root, text="location", font=("SF Pro", 30, "bold"), bg="systemTransparent", fg="white")
location_label.pack(padx=70, pady = 60)

img = ImageTk.PhotoImage(Image.open("/Users/tomassabol/Documents/python/weatherApp/cloudy.png").resize((260,250)))
img2 = ImageTk.PhotoImage(Image.open("/Users/tomassabol/Documents/python/weatherApp/night.png").resize((260,250)))
img3 = ImageTk.PhotoImage(Image.open("/Users/tomassabol/Documents/python/weatherApp/partly-cloudy.png").resize((260,250)))
img4 = ImageTk.PhotoImage(Image.open("/Users/tomassabol/Documents/python/weatherApp/rain.png").resize((260,250)))
img5 = ImageTk.PhotoImage(Image.open("/Users/tomassabol/Documents/python/weatherApp/snow.png").resize((260,250)))
img6 = ImageTk.PhotoImage(Image.open("/Users/tomassabol/Documents/python/weatherApp/storm.png").resize((260,250)))
img7 = ImageTk.PhotoImage(Image.open("/Users/tomassabol/Documents/python/weatherApp/sun.png").resize((260,250)))

image = Label(root, image=img, bg="#2a2a2a")
image.pack()

temperature_label = Label(root, text="temperature", font=("SF Pro", 25, "bold"), bg="#2a2a2a", fg="white")
temperature_label.pack(pady=20)

weather_prediction_label = Label(root, text="temperature", font=("SF Pro", 20, "bold"), bg="systemTransparent", fg="white")
weather_prediction_label.pack()




# frane to combine pack() && grid()
frame = Frame(root, bg = "#2a2a2a")


day1_label = Label(frame, bg = "#2a2a2a", fg="white")
temp1_label = Label(frame, bg = "#2a2a2a", fg="white")
day1_label.grid(row=0, column=0, padx=40)
temp1_label.grid(row=1, column=0, padx=40)

day2_label = Label(frame, bg = "#2a2a2a", fg="white")
temp2_label = Label(frame, bg = "#2a2a2a", fg="white")
day2_label.grid(row=0, column=1, padx=40)
temp2_label.grid(row=1, column=1, padx=40)

day3_label = Label(frame, bg = "#2a2a2a", fg="white")
temp3_label = Label(frame, bg = "#2a2a2a", fg="white")
day3_label.grid(row=0, column=2, padx=40)
temp3_label.grid(row=1, column=2, padx=40)

day4_label = Label(frame, bg = "#2a2a2a", fg="white")
temp4_label = Label(frame, bg = "#2a2a2a", fg="white")
day4_label.grid(row=0, column=3, padx=40)
temp4_label.grid(row=1, column=3, padx=40)


frame.pack(pady=60)


getWeather()
getDate()

root.mainloop()
