from django.shortcuts import render
import json
import urllib.request
# Create your views here.


def index(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        res = urllib.request.urlopen(
            "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=9f9ebd18b9f100bd162d10b419b243fe")
        json_data = json.loads(res.read())
        data = {
            "city": str(json_data["name"]),
            "country_code": str(json_data["sys"]["country"]),
            "coordinates": str((json_data["coord"]["lon"])) + ' ' + str(json_data["coord"]["lat"]),
            "temperature": str(json_data["main"]["temp"]),
            "pressure": str(json_data["main"]["pressure"]),
            "humidity": str(json_data["main"]["humidity"])
        }
    else:
        city = 'Empty'
        data = {}
    return render(request, 'index.html', data)
