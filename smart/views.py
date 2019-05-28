from django.shortcuts import render
# from django.http import HttpResponse
# from .models import Profile
from django.contrib.auth.decorators import login_required


def profile(request):
    return render(request, 'users/login2.html')

@login_required
def home(request):

    if request.user.is_staff:
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
    else:
        message = {}
        message["error"] = "Nie masz uprawnien do żadnej grupy."
        context = {
            'message': message
        }
        return render(request, 'smart/fail.html', context)


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
        if channel.device.name in devices:
            loc = devices[channel.device.name]
            # if not channel.name in loc:
            loc.append(channel.name)
            devices[channel.device.name] = loc
        else:
            loc = [channel.name]
            devices[channel.device.name] = loc

    # print(devices)
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
    return render(request, 'smart/device.html', context)