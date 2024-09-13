from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView, name = 'index'),
    path('login', views.LoginView, name = 'login'),
    path('logout', views.LogoutView, name = 'logout'),
    path('register', views.RegistrationView, name='register'),
]