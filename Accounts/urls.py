from django.contrib import admin
from django.urls import path, include
from .views import login, register, forgot, logout

urlpatterns = [
    path('entrar', login, name='login'),
    path('registrar', register, name='register'),
    path('logout', logout, name='logout'),
    path('esqueceu/senha', forgot, name='forgot'),
]
