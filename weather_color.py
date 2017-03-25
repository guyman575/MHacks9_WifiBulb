import urllib2
import json
import pyowm
def get_location():
    f = urllib2.urlopen('https://geoiptool.com/')
    web = f.read()
    f.close()
    latind = web.find('lat: ')
    lat = web[(latind + 5):].split(',')[0]
    lngind = web.find('lng: ')
    lng = web[(lngind + 5):].split(',')[0]
    return float(lat), float(lng)

def check_weather():
    owm = pyowm.OWM('5ce2439d46ef0c3b97aa6f3027142467')
    lat,lon = get_location()
    print lat, lon
    observation = owm.weather_at_coords(lat,lon)
    w = observation.get_weather()
    return str(w.get_weather_code())

def weather_to_color():
    weather = check_weather()
    if weather[0] == '2': #thunderstorm
        color = '25022C'
    elif weather[0] == '3': #drizzle
        color = '2262F6'
    elif weather[0] == '5': #rain
        color = '153787'
    elif weather[0] == '6': #snow
        color = '07F8FF'
    elif weather[0] == '7': #atmosphere
        color = '809E9F'
    elif weather == '800':#clear
        color = 'FFF700'
    elif weather[0] == '8': #cloudy
        color = '7FFFBF'
    elif weather[:2] == '90': #extreme
        color = 'FF0000'
    elif weather[0] == '9': #other random weather
        color = '00FF44'
    return color
