from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import CustomUser


class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(), label="Password", min_length=3)
    password2 = forms.CharField(widget=forms.PasswordInput(), label="Password confirmation", min_length=3)
    class Meta:
        model = CustomUser
        # model
        fields = ['username', 'password1', 'password2']
        help_texts = {
            'username': "",
            'password1': '',
            'password2': '',
        }
        # exclude = ('username.help_text', 'password.help_text',)

