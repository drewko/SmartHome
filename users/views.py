from django.shortcuts import render, redirect

# Create your views here.
from users.forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            # messages.success(request, f'Account created for {username}!')
            return redirect('smart-home')
    else:
        form = UserRegisterForm()
    return render(request, 'smart/templates/users/register.html', {'form': form})