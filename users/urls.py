from django.contrib.auth.views import  LogoutView
from django.urls import path

from users.views import AuthView, RegisterView

app_name = 'users'
urlpatterns = [
    path('login/', AuthView.as_view(template_name='users/login.html'), name='login'),
    path('register/', RegisterView.as_view(template_name='users/register.html'), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]