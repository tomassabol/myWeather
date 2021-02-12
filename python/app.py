from tkinter import *
from bs4 import BeautifulSoup
import requests

__author__ = "Tomas Sabol, https://www.github.com/tomassabol"

# setup window
root = Tk()
root.title("myWeather")
root.geometry("570x1212")


# var
background_image=PhotoImage("https://raw.githubusercontent.com/tomassabol/myWeather/main/python/images/sunny.png")
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)



root.mainloop()
