from django.urls import path
from . import views

urlpatterns = [
    path('locations/', views.locations, name='smart-locations'),
    path('', views.home, name='smart-home'),
    path('devices/', views.devices, name='smart-devices'),
    path('device/', views.device, name='smart-device'),
    path('getiovalue/',views.get_io_value,name='smart-getiovalue'),
    path('getivalue/',views.get_i_value,name='smart-getivalue'),
    path('setvalue/',views.setvalue,name='smart-setvalue'),
]