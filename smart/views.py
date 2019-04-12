from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile
from django.contrib.auth.decorators import login_required
# Create your views here.



def profile(request):
    return render(request, 'smart/login.html')


@login_required
def home(request):
    localizations={}


    for channel in request.user.profile_set.first().group.permissions.all():
        if channel.device.localization in localizations:
            localizations[channel.device.localization].append(channel)
        else:
            localizations[channel.device.localization]=[]
            localizations[channel.device.localization].append(channel)

    context={
        # 'channels':request.user.profile_set.first().group.permissions.all(),
        'localizations':localizations
    }
    return render(request, 'smart/home.html', context)