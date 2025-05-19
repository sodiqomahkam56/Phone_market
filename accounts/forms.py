from django import forms
from .models import CustomUser


class UserForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = [
            'username',
            'email',
            'phone',
            'password',
                  ]


    def save(self, commit=True):
        user = CustomUser.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            phone=self.cleaned_data['phone'],
            email=self.cleaned_data['email'],
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


class ForgetForm(forms.Form):
    username=forms.CharField(required=True)


class PasswordResetForm(forms.Form):
    code=forms.CharField(required=True)
    password=forms.CharField(required=True)
    re_password = forms.CharField(required=True)