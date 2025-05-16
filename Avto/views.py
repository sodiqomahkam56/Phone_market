from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render, redirect
from .forms import PhoneForm
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




def logout(request):
    logout(request)
    return redirect('login')









