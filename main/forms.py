# from importlib._common import _

from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserChangeForm
from django.core.exceptions import ValidationError

from .apps import user_registered
from .models import AdvUser


class MinMaxValidator:
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, value):
        if self.min_length > len(value) or len(value) > self.max_length:
            raise ValidationError('Введенное число должно находится в пределах от %(min)s '
                                  '%(max)s ',
                                  code='out_of_range',
                                  params={'min': self.min_length, 'max': self.max_length})


class AdvForm(forms.ModelForm):
    email = forms.EmailField(label='Адрес электронной почты', required=True)

    class Meta:
        model = AdvUser
        fields = ('username', 'email', 'first_name', 'last_name', 'send_message')


class RegisterUserForm(AdvForm):
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput,
                                help_text=password_validation.password_validators_help_text_html())

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError('Введенные пароли не совпадают',
                                  code='password_mismatch')
        password_validation.validate_password(password2)
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_active = False
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        user_registered.send(RegisterUserForm, instance=user)
        return user

    class Meta(AdvForm.Meta):
        fields = ('username', 'password1', 'password2', 'email',
                  'first_name', 'last_name', 'send_message')


class AdminRegisterUserForm(UserChangeForm, RegisterUserForm):
    class Meta(RegisterUserForm.Meta):
        pass
