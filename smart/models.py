from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db import models
from enum import Enum


class Localization(models.Model):
    name = models.CharField(max_length=256)
    def __str__(self):
        return self.name

class Device(models.Model):
    name = models.CharField(max_length=256)
    localization = models.ForeignKey(Localization, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.name}'

class ChannelType(Enum):
    Input='input'
    InputOutput='input/output'
    Output='output'

class Channel(models.Model):
    device = models.ForeignKey(Device , on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    type = models.CharField(max_length=20, choices=[(tag.name, tag.value) for tag in ChannelType])

    def __str__(self):
        return f'{self.device} -> {self.name} {self.type}'


class Group(models.Model):
    name = models.CharField(max_length=20)

    permissions = models.ManyToManyField(Channel, related_name="permissions", blank=True)

    def __str__(self):
        return f'{self.name} Group'

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'