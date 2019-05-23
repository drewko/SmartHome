from django.contrib import admin
from .models import CustomUser, Group, Device, Channel, Location
from django.contrib.auth.models import AbstractUser
# Rester your models here.

admin.site.register(Group)
admin.site.register(CustomUser)
admin.site.register(Device)
admin.site.register(Channel)
admin.site.register(Location)
