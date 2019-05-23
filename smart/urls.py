from django.urls import path
from . import views

urlpatterns = [
    path('locations/', views.locations, name='smart-locations'),
    path('', views.home, name='smart-home'),
    path('devices/', views.devices, name='smart-devices'),
    path('device/', views.device, name='smart-device')
]