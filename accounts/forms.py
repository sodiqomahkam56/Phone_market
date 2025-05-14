from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    # fullname = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username','password']

    # def save(self, commit=True):
        # user = super().save(commit=False)
        # fullname = self.cleaned_data['fullname'].strip()
        # parts = fullname.split(' ', 1)
        # user.first_name = parts[0]
        # user.last_name = parts[1] if len(parts) > 1 else ''
        # user.set_password(self.cleaned_data['password'])  # Shifrlash
        # if commit:
        #     user.save()
        # return user

    def save(self, commit=True):
        return User.objects.create_user(self.cleaned_data['username'],self.cleaned_data['password'])

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
