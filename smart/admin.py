from django.contrib import admin
from .models import Profile, Group, Permmision, Device, Channel
# Rester your models here.

admin.site.register(Profile)
admin.site.register(Group)
admin.site.register(Permmision)

admin.site.register(Device)
admin.site.register(Channel)
