from django.shortcuts import render
import requests

# Create your views here.


# Making use of foreign API
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=63020976186acf2ec370d8d3db8c8ad5'

    if request.method == 'GET':
        city_weather = {
            'city': 'Nepal',
            'temperature': '100',
            'description': 'This is dummy data',
            'icon': '09n',
        }

        context = {'city_weather': city_weather}
        return render(request, 'weather.html', context)

    elif request.method == 'POST':
        city = request.POST.get('cityname')
        r = requests.get(url.format(city)).json()

        city_weather = {
            'city': city,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }
        print(city_weather)

        context = {'city_weather': city_weather}

        return render(request, 'weather.html', context)


# making use of nepali API
def home(request):
    url = 'https://nepal-weather-api.herokuapp.com/api/?place=Birendranagar'
    if request.method == 'GET':
        temperature = {
            'city': 'Nepal',
            'max': '100° C',
            'min': '0° C',
            'rainfall': 'Dummy Data'
        }
        context = {
            'temperature': temperature
        }
        return render(request, 'temperature.html', context)
    else:
        city = request.POST.get('cityname')
        r = requests.get(url.format(city)).json()
        # print(r['place']) remove the comment to check the data received
        temperature = {
            'city': city,
            'max': r['max'],
            'min': r['min'],
            'rainfall': r['rain']
        }
        context = {
            'temperature':temperature
        }
        return render(request, 'temperature.html', context)