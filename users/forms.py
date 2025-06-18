from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import forms

from users.models import User

class StyleFormMixin(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class LoginForm(StyleFormMixin,AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')


from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, EmailValidator
from django.contrib.auth.forms import UserCreationForm
from users.models import User
import re

class StyleFormMixin(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

def validate_cyrillic_name(value):
    if not re.match(r'^[А-Яа-яЁё\s]+$', value):
        raise ValidationError("Поле должно содержать только кириллицу и пробелы.")

class RegisterForm(StyleFormMixin, UserCreationForm):
    email = forms.EmailField(validators=[EmailValidator()], label="Email")
    phone = forms.CharField(
        max_length=17,
        validators=[
            RegexValidator(r'^\+7\(\d{3}\)-\d{3}-\d{2}-\d{2}$', message="Формат: +7(XXX)-XXX-XX-XX")
        ],
        label="Телефон",
        widget=forms.TextInput(attrs={
            'placeholder': '+7(XXX)-XXX-XX-XX'
        })
    )
    first_name = forms.CharField(validators=[validate_cyrillic_name], label="Имя")
    last_name = forms.CharField(validators=[validate_cyrillic_name], label="Фамилия")
    middle_name = forms.CharField(validators=[validate_cyrillic_name], label="Отчество")
    password1 = forms.CharField(min_length=6, widget=forms.PasswordInput, label="Пароль")
    password2 = forms.CharField(min_length=6, widget=forms.PasswordInput, label="Повторите пароль")

    class Meta:
        model = User
        fields = ('username', 'last_name', 'first_name', 'middle_name', 'email', 'phone', 'password1', 'password2')
