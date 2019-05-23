from django.contrib import admin

from .models import Group, Device, Channel, Localization

# Rester your models here.

admin.site.register(Group)
admin.site.register(Device)
admin.site.register(Channel)
admin.site.register(Localization)
