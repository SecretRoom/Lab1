import pyowm

print('OpenWeatherMap')

owm = pyowm.OWM('dd05ec13d4ca84faa51aa31bf35e653a')
observation = owm.weather_at_place('Rostov-on-Don,ru')
weather = observation.get_weather()
location = observation.get_location()
translate = {'Rostov-on-Don': 'Ростов-на-Дону'}

print('Страна :'+location.get_country())
print ('Город :'+translate[location.get_name()])
print('Долгота :' +str(location.get_lon()))
print('Широта :' +str(location.get_lat()))
print('Облачность :'+str(weather.get_clouds()))
print('Статус :'+str(weather.get_detailed_status()))
print('Дождь :'+str(weather.get_rain()))
print('Снег :'+str(weather.get_snow()))
print('Время :'+str(weather.get_reference_time('iso')))
print('Статус :'+str(weather.get_status()))
print('Восход :'+str(weather.get_sunrise_time('iso')))
print('Закат :'+str(weather.get_sunset_time('iso')))
print('Температура :'+str(weather.get_temperature('celsius')))
print('Видимость ;'+str(weather.get_visibility_distance()))
print('Изображение :'+weather.get_weather_icon_name())
print('Ветер :'+str(weather.get_wind()))