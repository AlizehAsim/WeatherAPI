#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
from flask import Flask, render_template

app = Flask(__name__)
 
@app.route("/")
def hello():
    location = requests.get('https://ipinfo.io/')
    location_data = location.json()
    city = location_data['city']
    country = location_data['country']
    weather = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city+','+country+'&appid=d583544f1369c5dfb4016d7d3ef47e0e&units=imperial')

    weather_data = weather.json()
    temperature = weather_data['main']['temp']
    
    response = "Current Temperature (F) in "
    response += str(city)
    response += " is: "
    response += str(temperature)
    
    return (response)

if __name__ == "__main__":
    app.run()

