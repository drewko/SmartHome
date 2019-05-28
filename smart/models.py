from enum import Enum

from django.contrib.auth.models import AbstractUser
from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Device(models.Model):
    name = models.CharField(max_length=256, unique=True)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.name}'


class ChannelType(Enum):
    Input = 'input'
    InputOutput = 'input/output'


class Channel(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    name = models.CharField(max_length=256, unique=True)
    type = models.CharField(max_length=20, choices=[(tag.name, tag.value) for tag in ChannelType])
    status = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.device} -> {self.name} {self.type}'


class Group(models.Model):
    name = models.CharField(max_length=20)
    permissions = models.ManyToManyField(Channel, related_name="permissions", blank=True)

    def __str__(self):
        return f'{self.name}'
