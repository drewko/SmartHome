from django.contrib import admin
from django.urls import path, include
from SmartHome import mqtt
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('smart.urls')),
    path('', include('users.urls')),
]

mqtt.client.loop_start()
