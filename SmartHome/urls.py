from django.contrib.auth import views as auth_view
from users import views as user_views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import  static
from SmartHome import mqtt
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('smart.urls')),
    path('', include('users.urls')),
]

mqtt.client.loop_start()
