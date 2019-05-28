import json
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from SmartHome import mqtt

from smart.models import Channel


def profile(request):
    return render(request, 'smart/../users/templates/users/login.html')


@login_required
def home(request):
    locations = {}

    for channel in request.user.group.permissions.all():
        if channel.device.location in locations:
            locations[channel.device.location].append(channel)
        else:
            locations[channel.device.location]=[]
            locations[channel.device.location].append(channel)

    context={
        'locations': locations
    }
    return render(request, 'smart/home.html', context)


@login_required
def locations(request):
    locations = {}

    for channel in request.user.group.permissions.all():
        if channel.device.location in locations:
            loc = locations[channel.device.location]
            if not channel.device.name in loc:
                loc.append(channel.device.name)
            locations[channel.device.location] = loc
        else:
            loc = [channel.device.name]
            locations[channel.device.location] = loc

    context = {
        'locations': locations
    }
    return render(request, 'smart/locations.html', context)


@login_required
def devices(request):
    devices = {}

    for channel in request.user.group.permissions.all():
        if channel.device not in devices:
            devices[channel.device]=[]
            devices[channel.device].append(channel)
        else:
            devices[channel.device].append(channel)

    context = {
        'devices': devices
    }
    return render(request, 'smart/devices.html', context)


@login_required
def device(request):
    deviceId = request.GET.get('device')
    print(deviceId)
    channels = []
    for channel in request.user.group.permissions.all():
        if channel.device.id == int(deviceId):
            channels.append(channel)
            print('added ' + str(channel) + 'channel to channels')
    context = {
        'channels': channels
    }
    return render(request, 'smart/device.html', context)\

@login_required
def get_io_value(request):
    response = HttpResponse(content_type="text/plain")
    if request.method == 'POST':
        body = json.loads(request.body)
        target = Channel.objects.get(name=body['channel'], device__name=body['device'])
        if request.user.is_authenticated and target in request.user.group.permissions.all():
            status = Channel.objects.get(name=body['channel'], device__name=body['device']).status
            response.content = status
            response.status_code = 200
        else:
            response.status_code = 403
        return response
    else:
        response.status_code = 503
        return response

@login_required
def get_i_value(request):
    response = HttpResponse(content_type="text/plain")
    if request.method == 'POST':
        body = json.loads(request.body)
        target = Channel.objects.get(name=body['channel'], device__name=body['device'])
        if request.user.is_authenticated and target in request.user.group.permissions.all() and target.type == 'Input':
            mqtt.client.publish('/' + body['device'] + '/' + body['channel'], 'status')
            status = Channel.objects.get(name=body['channel'], device__name=body['device']).status
            response.content = status
            response.status_code = 200
        else:
            response.status_code = 403
        return response
    else:
        response.status_code = 503
        return response

@login_required
def setvalue(request):
    response = HttpResponse(content_type="text/plain")
    if request.method == 'POST':
        body = json.loads(request.body)
        target = Channel.objects.get(name=body['channel'], device__name=body['device'])
        if request.user.is_authenticated and target in request.user.group.permissions.all():
            mqtt.client.publish('/'+body['device']+'/'+body['channel'], body['value'])
            response.status_code = 200
        else:
            response.status_code = 403
        return response
    else:
        response.status_code = 503
        return response

