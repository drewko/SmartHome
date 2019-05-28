from django.contrib.auth import views as auth_view
from django.urls import path

from users import views as user_views

urlpatterns = [
    # path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='users/register2.html'), name='logout'),
    path('register/', user_views.register, name='register'),
    path('login/', auth_view.LoginView.as_view(template_name='users/login2.html'), name='login'),
]
