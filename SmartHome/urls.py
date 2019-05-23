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
    path('login/', auth_view.LoginView.as_view(template_name='smart/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='smart/logout.html'), name='logout'),
    path('register/', user_views.register, name='register'),
]

# mqtt.client.loop_start()
