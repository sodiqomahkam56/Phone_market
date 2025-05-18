from django import forms
from .models import CustomUser


class UserForm(forms.ModelForm):
    # fullname = forms.CharField(max_length=100)

    class Meta:
        model = CustomUser
        fields = ['username','phone','password',]

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
        user = CustomUser.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            phone=self.cleaned_data['phone']
        )
        return user


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class EmailForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    from_email = forms.EmailField()
    to_email = forms.EmailField()

