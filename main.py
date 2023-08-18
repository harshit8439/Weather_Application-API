from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city=city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=71045d1412213351d17bcd1320558c78").json()
    w_label1.config(text=data["weather"][0]["main"])
    Des_label1 .config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
    Pres_label1.config(text=data["main"]["pressure"])

win = Tk()
win.title("Weather Wizard")
win.config(bg="black")
win.geometry("500x500")

name_label = Label(win, text="Welcome To Weather Wizard", fg="cyan", bg="black", font=("Times New Roman", 25, "bold"))
name_label.place(x=25, y=50, height=50, width=450)

city_name=StringVar()
list_name = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal", "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli", "Daman and Diu", "Lakshadweep", "National Capital Territory of Delhi", "Puducherry"]

com = ttk.Combobox(win, values=list_name, font=("Times New Roman", 20, "bold"),textvariable=city_name)
com.place(x=50, y=120, height=40, width=400)


w_label = Label(win, text="Weather Climate", fg="black", bg="white", font=("Times New Roman", 13,"bold"))
w_label.place(x=25, y=260, height=50, width=210)

w_label1 = Label(win, text="", fg="black", bg="white", font=("Times New Roman", 13,"bold"))
w_label1.place(x=260, y=260, height=50, width=210)


temp_label = Label(win, text="Temperature", fg="black", bg="white", font=("Times New Roman", 13,"bold"))
temp_label.place(x=25, y=330, height=50, width=210)

temp_label1= Label(win, text="", fg="black", bg="white", font=("Times New Roman", 13,"bold"))
temp_label1.place(x=260, y=330, height=50, width=210)

Pres_label = Label(win, text="Pressure", fg="black", bg="white", font=("Times New Roman", 13,"bold"))
Pres_label.place(x=25, y=400, height=50, width=210)


Pres_label1 = Label(win, text="", fg="black", bg="white", font=("Times New Roman", 13,"bold"))
Pres_label1.place(x=260, y=400, height=50, width=210)

Des_label = Label(win, text="Description", fg="black", bg="white", font=("Times New Roman", 13,"bold"))
Des_label.place(x=25, y=470, height=50, width=210)

Des_label1 = Label(win, text="", fg="black", bg="white", font=("Times New Roman", 13,"bold"))
Des_label1.place(x=260, y=470, height=50, width=210)

check_button=Button(win,text="Check Weather",font=("Times New Roman",15,"bold"),command=data_get)
check_button.place(y=190,height=40,width=150,x=180)
win.mainloop()
