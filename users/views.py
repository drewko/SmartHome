from django.shortcuts import render, redirect

# Create your views here.
from users.forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            # messages.success(request, f'Account created for {username}!')
            return redirect('smart-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register2.html', {'form': form})