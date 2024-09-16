from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('Signup', views.signup, name="signup"),
    path('Login', views.login, name="login")
]
