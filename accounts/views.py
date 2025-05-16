from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from accounts.forms import UserForm, LoginForm, EmailForm


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.filter(username=username).first()
            print(user)
            if user:
                login(request, user)
                print(user)
                return redirect('phone-list')
            else:
                form.add_error(None, "Login yoki parol noto‘g‘ri")
    else:
        form = LoginForm(request.POST)

    return render(request, 'accounts/login.html', {'form': form})

def send_email(request):
    form=EmailForm()
    return render(request, 'accounts/send_email.html', {'form': form})

