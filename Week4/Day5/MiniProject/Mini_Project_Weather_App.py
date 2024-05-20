from pyowm.owm import OWM
import matplotlib
import tkinter

def get_forecast(city):
    owm = OWM('ff2723c8cd446d052df25607ff1c159f')
    mgr = owm.weather_manager()
    reg = owm.city_id_registry()
    city = reg.ids_for(city, matching='exact')[0]
    city_id, city_name, country = city[0], city[1], city[2]
    observation = mgr.weather_at_place(f"{city_name}, {country}")
    weather = observation.weather
    wind = observation.weather.wind()
    sunrise_time = weather.sunrise_time('iso')
    sunset_time = weather.sunset_time('iso')
    
    print(f"Current weather in {city_name}: {weather.status}, {weather.temperature('celsius')['temp']}°C")
    print(f"Wind speed: {wind['speed']} m/s")
    print(f"Sunrise time: {sunrise_time}")
    print(f"Sunset time: {sunset_time}")

    three_h_forecast = mgr.forecast_at_id(city_id, '3h')
    for weather in three_h_forecast.forecast:
        print(weather.reference_time('iso'), weather.detailed_status)
    

city = input('Please enter your city: ')
get_forecast(city)