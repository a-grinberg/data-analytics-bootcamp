from pyowm.owm import OWM

owm = OWM('ff2723c8cd446d052df25607ff1c159f')
mgr = owm.weather_manager()
observation = mgr.weather_at_place("Tel-Aviv, IL")
weather = observation.weather
wind = observation.weather.wind
sunrise_time = weather.sunrise_time('iso')
sunset_time = weather.sunset_time('iso')


print(f"Current weather in Tel Aviv: {weather.status()}, {weather.temperature('celsius')['temp']}°C")
print(f"Wind speed: {wind['speed']} m/s")
print(f"Sunrise time: {sunrise_time}")
print(f"Sunset time: {sunset_time}")

