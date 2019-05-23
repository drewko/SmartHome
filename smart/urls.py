from django.urls import path
from . import views

urlpatterns = [
    path('locations/', views.locations, name='smart-locations'),
    path('', views.home, name='smart-home'),
]