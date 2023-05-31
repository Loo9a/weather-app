import tkinter as tk 
import requests
import time

def getweather(canvas):
    city = textfield.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city +"&appid=e33f91800cb7428ccce90bae428e55cf"
    JASON_DATA = requests.get(api).json()
    condition = JASON_DATA['weather'][0]['main']
    temp = int(JASON_DATA['main']['temp'] - 273.15)
    min_temp = int(JASON_DATA['main']['temp_min'] - 273.15)
    max_temp = int(JASON_DATA['main']['temp_max'] - 273.15)
    pressure = JASON_DATA['main']['pressure']
    humidity = JASON_DATA['main']['humidity']
    wind = JASON_DATA['wind']['speed']

    final_info = condition + "\n" + str(temp) + "°C"
    final_data = "\n" + "Max Temp : " + str(max_temp) + "\n" + "Min Temp : " + str(min_temp)
    label1.config(text = final_info)
    label2.config(text = final_data)



canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")

f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textfield = tk.Entry(canvas, justify='center', font= t)
textfield.pack(pady= 20)
textfield.focus()
textfield.bind('<Return>', getweather)

label1 = tk.Label(canvas, font= t)
label1.pack()

label2 = tk.Label(canvas, font= f)
label2.pack()

canvas.mainloop()