import requests
import datetime

city_name = input('input city')

API_key = '70eeae1322ccc585e1ee950c130ba7f4'

API = f'https://api.openweathermap.org/data/2.5/weather?' \
      f'q={city_name}&appid={API_key}&units=metric'

response = requests.get(API).json()

data = {}
data['City'] = response['name']
data['Temperature'] = f"{response['main']['temp']} °C"
data['Wind'] = f"{response['wind']['speed']} m/s"
data['Clouds'] = f"{response['clouds']['all']} %"
data['Humidity'] = f"{response['main']['humidity']} %"
data['Pressure'] = f"{response['main']['pressure']} Pa"
sunrise = datetime.datetime.fromtimestamp(response['sys']['sunrise'])
data['Sunrise'] = sunrise.__str__().split(' ')[1]
sunset = datetime.datetime.fromtimestamp(response['sys']['sunset'])
data['Sunset'] = sunset.__str__().split(' ')[1]

for k, v in data.items():
    print(f'{k}: {v}')
