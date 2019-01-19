# quick_weather.py - Prints the weather for a location from the command line.


import json, requests, sys


if len(sys.argv) < 2:
    print('Usage: quick_weather.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])

url = 'http://api.openweather.org/data/2.5/forecast/daily?q={}&cnt=3'.format(location)

response = requests.get(url)
response.raise_for_status()

weather_data = json.loads(response.text)

w = weather_data['list']
print('Current weather in {}:'.format(location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])

