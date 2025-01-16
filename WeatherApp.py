from configparser import ConfigParser
import requests
from tkinter import *
from tkinter import messagebox

# extracting the key from config file
config_file = r"C:\Users\muniz\OneDrive - Temple University\Desktop\Random Projects\Various-Projects\config.ini"
config = ConfigParser()
config.read(config_file)
api_key = config['Weather']['api']
url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

# Function to get the weather details
def getweather(city):
    result = requests.get(url.format(city, api_key))

    if result:
        json = result.json()
        city = json['name']
        country = json['sys']['country']
        temp_kelvin = json['main']['temp']
        temp_celsious = temp_kelvin - 273.15
        weather1 = json['weather'][0]['main']
        final = [city, country, temp_kelvin, temp_celsious, weather1]
        return final
    else:
        print("No Content Found")
    
# Function to search for the city
def search():
    city = city_text.get()
    weather = getweather(city)
    if weather:
        location_lbl['text'] = '{} ,{}'.format(weather[0], weather[1])
        temperature_label['text'] = str(weather[3])+"   Degree Celsius"
        weather_l['text'] = weather[4]
    else:
        messagebox.showerror('Error', "Cannot find {}".format(city))


# Main code

# Creating the main app
app = Tk()

app.title("Weather App")

app.geometry("300x300") # Window size

city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack()

# Adding various labels and buttons to the app
Search_btn = Button(app, text= "Search Weather", width=12, command=search)
Search_btn.pack()

location_lbl = Label(app, text= "Location", font = ('bold', 2))
location_lbl.pack()

temperature_label = Label(app, text = "")
temperature_label.pack()

weather_l = Label(app, text = "")
weather_l.pack()

app.mainloop()
