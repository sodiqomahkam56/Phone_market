from django.contrib.auth import logout
from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render, redirect
from .forms import PhoneForm
from .models import Profile
from .models import Phone


def create_phone(request):
    if request.method == "POST":
        brand = request.POST['brand']
        model = request.POST['model']
        price = request.POST['price']
        if brand and model and price:
            Phone.objects.create(brand=brand, model=model, price=price)
            return redirect('phone-list')
    return render(request, 'phone/phone.html')

def phone_list(request):
    phones = Phone.objects.all()
    return render(request, 'phone/phone_list.html', {'phones': phones})

def phone_create(request):
    if request.method == "POST":
        form = PhoneForm(request.POST, request.FILES)  # request.FILES qo‘shildi
        if form.is_valid():
            form.save()
            return redirect('phone-list')
    else:
        form = PhoneForm()
    return render(request, 'phone/phone_form.html', {'form': form})



def phone_detail(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    phone = Phone.objects.get(id=id)
    context = {
        'phone': phone,
    }
    return render(request, 'phone/phone_detail.html', context)


def phone_delete(request, id):
    phone = Phone.objects.get(id=id)
    if request.method == "POST":
        phone.delete()
        return redirect('phone-list')
    return HttpResponseNotAllowed(['POST'])


from django.shortcuts import get_object_or_404, redirect, render
from .models import Phone


def update_phone(request,pk):
    phone=Phone.objects.get(pk=pk)
    if request.method == "POST":
        form=PhoneForm(request.POST,request.FILES, instance=phone)
        if form.is_valid():
            form.save()
            return redirect('phone-list')
        else:
            return HttpResponse('Notogri malumot kiritgansiz',status=400)
    else:
        form=PhoneForm(instance=phone)
    return render(request, 'phone/phone_form.html', {'form': form}) #html yaratish kerak




def logout_view(request):
    logout(request)
    return redirect('login')


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def user_account(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)

    if request.method == "POST":
        first_name = request.POST.get('name')
        phone = request.POST.get('phone')
        avatar = request.FILES.get('avatar')

        if first_name:
            user.first_name = first_name
            user.save()

        if phone is not None:
            profile.phone = phone

        if avatar is not None:
            profile.avatar = avatar

        profile.save()

        request.session['profile_edit_mode'] = False
        return redirect('user-account')

    edit_mode = request.session.get('profile_edit_mode', False)

    context = {
        'user': user,
        'profile': profile,
        'edit_mode': edit_mode,
    }
    return render(request, 'phone/user_account.html', context)


@login_required
def profile_edit_mode(request):
    request.session['profile_edit_mode'] = True
    return redirect('user-account')






