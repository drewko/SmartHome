from django.shortcuts import render
# from django.http import HttpResponse
# from .models import Profile
from django.contrib.auth.decorators import login_required


# Create your views here.


def profile(request):
    return render(request, 'smart/login.html')


@login_required
def home(request):
    locations = {}
    for channel in request.user.group.permissions.all():
        if channel.device.location in locations:
            locations[channel.device.location].append(channel)
        else:
            locations[channel.device.location] = []
            locations[channel.device.location].append(channel)

    context = {
        # 'channels':request.user.profile_set.first().group.permissions.all(),
        'locations': locations
    }
    return render(request, 'smart/home.html', context)


@login_required
def devices(request):
    devices = []

    for channel in request.user.group.permissions.all():
        if channel.device not in devices:
            devices.append(channel.device)

    context = {
        # 'channels':request.user.profile_set.first().group.permissions.all(),
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
        # 'channels':request.user.profile_set.first().group.permissions.all(),
        'channels': channels
    }
    return render(request, 'smart/device.html', context)
