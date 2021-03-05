from allauth.account.forms import SignupForm
from django import forms as as_forms

from django.contrib.auth import forms
from .models import User
from .validate import validate_CPF, validate_Telefone


class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = User


class MyCustomSignupForm(SignupForm):
    first_name = as_forms.CharField(max_length=30, label='Nome')
    last_name = as_forms.CharField(max_length=30, label='Sobrenome')
    cpf = as_forms.CharField(max_length=11, label='CPF', validators=[validate_CPF])
    phone = as_forms.CharField(max_length=11, label='Telefone', validators=[validate_Telefone])

    def __init__(self, *args, **kwargs):
        super(MyCustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget = as_forms.TextInput(attrs={'placeholder': 'Nome'})
        self.fields['last_name'].widget = as_forms.TextInput(attrs={'placeholder': 'Sobrenome'})
        self.fields['cpf'].widget = as_forms.TextInput(attrs={'placeholder': 'CPF'})
        self.fields['phone'].widget = as_forms.TextInput(attrs={'placeholder': 'Telefone'})

    def save(self, request):
        user = super(MyCustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.cpf = self.cleaned_data['cpf']
        user.phone = self.cleaned_data['phone']
        user.save()
        return user
