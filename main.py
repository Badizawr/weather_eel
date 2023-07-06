import eel
import pyowm
import requests

@eel.expose
def get_weather(place):
    url = 'https://api.openweathermap.org/data/2.5/weather?q='+place+'&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'
    weather_data = requests.get(url).json()
    temperature = round(weather_data['main']['temp'])
    return'Сейчас в городе', place, str(temperature), '°C'

#place = 'Хабаровск'
#url = 'https://api.openweathermap.org/data/2.5/weather?q='+place+'&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'
#weather_data = requests.get(url).json()
#temperature = round(weather_data['main']['temp'])
#print('Сейчас в городе', place, str(temperature), '°C')

if __name__ == '__main__':
    eel.init("web")
    eel.start("main.html",mode ="chrome", size=(760, 760))
