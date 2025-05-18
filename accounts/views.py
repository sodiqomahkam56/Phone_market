from random import randint, random
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from accounts.forms import UserForm, LoginForm, EmailForm
from .models import CustomUser


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print(form.errors)
            return render(request, 'accounts/register.html', {'form': form})
    else:
        form = UserForm()
    return render(request, 'accounts/register.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            if CustomUser.objects.filter(username=username).exists():
                messages.error(request, 'Bu username band, iltimos boshqa username tanlang.')
                # username band bo‘lsa, formni qayta ko‘rsatamiz xatolik bilan
                return render(request, 'accounts/register.html', {'form': form})
            else:
                form.save()
                messages.success(request, 'Ro‘yxatdan o‘tish muvaffaqiyatli yakunlandi!')
                return redirect('login')
        else:
            messages.error(request, 'Iltimos, shaklni to‘g‘ri to‘ldiring.')
    else:
        form = UserForm()
    return render(request, 'accounts/register.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            print(user)
            if user:
                login(request, user)
                print(user)
                return redirect('phone-list')
            else:
                form.add_error(None, "Login yoki parol noto‘g‘ri")
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})

def send_email(request):
    form=EmailForm()
    return render(request, 'accounts/send_email.html', {'form': form})

def random_number():
    return random.randint(100000,999999)