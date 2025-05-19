from random import randint, random
from django.contrib import messages
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect

from Avto.models import Code
from Avtomobil.settings import EMAIL_HOST_USER as from_email
from accounts.forms import UserForm, LoginForm, EmailForm, ForgetForm, PasswordResetForm
from .models import CustomUser
from .utils import send_html_email



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


def forget_view(request):
    if request.method == 'POST':
        form = ForgetForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            user = CustomUser.objects.filter(username=username).first()
            if user is not None:
                code=Code.objects.create(user=user)
                send_html_email(
                    subject="Parol tiklash",
                    from_email=from_email,
                    to_email=user.email,
                    verification_code=code.code,
                    username=user.username,
                )
                return render(request, 'accounts/done.html', {'form': form})

    form=ForgetForm()
    return render(request, 'accounts/forget_view.html', {'form': form})


def change_password_view(request):
    form = PasswordChangeForm(request.user, request.POST)
    if form.is_valid():
        user=form.save()
        update_session_auth_hash(request, user)
        messages.success(request, 'Parolingiz muvaffaqiyatli o‘zgartirildi.')
        return redirect('login')
    else:
        print(request.user, request.user.is_authenticated)
        messages.error(request, 'Iltimos, kodni to‘g‘rilang.')
    form=PasswordResetForm()
    return render(request, 'accounts/change_password.html', {'form': form})
