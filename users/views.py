from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import LoginForm, RegisterForm
from users.models import User


# Create your views here.
class AuthView(LoginView):
    form_class = LoginForm

class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    success_url = reverse_lazy('users:login')
