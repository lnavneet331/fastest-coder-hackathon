#create a function that takes a city's name as input and uses openweathermap api to return the current temperature in that city

import requests
import json

def get_temp(city):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=b3c6330faf009dabb64f7acde1e13c4f'.format(city)
    response = requests.get(url)
    data = response.json()
    #round the temperatture to only 2 decimal places
    temp = round(data['main']['temp'] - 273.15, 2)
    return temp


#gitbub copilot created the get_temp function, and then we only needed to customize the function according to our need