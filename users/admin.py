from django.contrib import admin

# Register your models here.
from users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    fields = ("username", "group", "is_active")
