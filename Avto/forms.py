from operator import truediv

from django import forms

from Avto.models import Phone


class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = ['brand', 'model', 'price','image','description',]
        widgets = {
            'brand': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masalan: Samsung'}),
            'model': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masalan: Galaxy S23'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Masalan: 999'}),
        }

