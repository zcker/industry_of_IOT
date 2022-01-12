from django.shortcuts import render
from sim_industry.models import Weight, Gas, Temperature, DeviceInfo, Door, Fire, Water
import json
from django.shortcuts import render, HttpResponse
import requests


# Create your views here.

def weight_info(request):
    if request.method == 'POST':
        weight = Weight.objects.all()
        timeList = []
        weightList = []
        for keyvalue in weight:
            _time = keyvalue.time.strftime('%Y-%m-%d')
            _value = keyvalue.value
            timeList.append(str(_time))
            weightList.append(_value)

        result = json.dumps({'w_times': timeList, 'w_values': weightList})
        return HttpResponse(result, content_type='application/json')

    return render(request, 'weight.html', locals())


def gas_info(request):
    if request.method == 'POST':
        gas = Gas.objects.all()
        timeList = []
        gasList = []
        for keyvalue in gas:
            _time = keyvalue.time.strftime('%Y-%m-%d')
            _value = keyvalue.value
            timeList.append(str(_time))
            gasList.append(_value)

        result = json.dumps({'g_times': timeList, 'g_values': gasList})
        return HttpResponse(result, content_type='application/json')

    return render(request, 'gas.html', locals())


def temperature_info(request):
    if request.method == 'POST':
        temperature = Temperature.objects.all()
        timeList = []
        temList = []
        for keyvalue in temperature:
            _time = keyvalue.time.strftime('%Y-%m-%d')
            _value = keyvalue.value
            timeList.append(str(_time))
            temList.append(_value)

        result = json.dumps({'t_times': timeList, 't_values': temList})
        return HttpResponse(result, content_type='application/json')

    return render(request, 'temperature.html', locals())


def index_info(request):
    if request.method == 'POST':
        device = DeviceInfo.objects.all()
        device_info = []
        for i in device:
            device_info.append(i.id)
            device_info.append(i.title)
            device_info.append(i.description)
            device_info.append(i.online)
            device_info.append(i.encrypt)
            device_info.append(i.onlinetime)

        result = json.dumps({'info': device_info})
        return HttpResponse(result, content_type='application/json')
    return render(request, 'index.html', locals())


def door_info(request):
    if request.method == 'POST':
        door = Door.objects.last()
        door_info = []
        door_info.append(door.time.strftime('%Y-%m-%d %H:%M:%S'))
        door_info.append(door.value)
        result = json.dumps({'door': door_info})
        return HttpResponse(result, content_type='application/json')
    return render(request, 'index.html', locals())


def fire_info(request):
    if request.method == 'POST':
        fire = Fire.objects.last()
        fire_info = []
        fire_info.append(fire.time.strftime('%Y-%m-%d %H:%M:%S'))
        fire_info.append(fire.value)
        result = json.dumps({'fire': fire_info})
        return HttpResponse(result, content_type='application/json')
    return render(request, 'index.html', locals())


def water_info(request):
    if request.method == 'POST':
        water = Water.objects.last()
        water_info = []
        water_info.append(water.time.strftime('%Y-%m-%d %H:%M:%S'))
        water_info.append(water.value)
        result = json.dumps({'water': water_info})
        return HttpResponse(result, content_type='application/json')
    return render(request, 'index.html', locals())


def play(request):
    payload = {
        'access_token': 'd87a19e48c52caf9a97bffcdd6c3845a0f1b4e2d',
        'id': 'D24409',
        'c': 'play'
    }
    url = 'https://www.bigiot.net/oauth/say'
    response = requests.post(url, payload)
    print(response.content.decode(encoding="utf-8-sig"))
    return render(request, 'index.html', locals())

def pause(request):
    payload = {
        'access_token': 'd87a19e48c52caf9a97bffcdd6c3845a0f1b4e2d',
        'id': 'D24409',
        'c': 'pause'
    }
    url = 'https://www.bigiot.net/oauth/say'
    response = requests.post(url, payload)
    print(response.content.decode(encoding="utf-8-sig"))
    return render(request, 'index.html', locals())
