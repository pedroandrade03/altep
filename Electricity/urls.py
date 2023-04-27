from django.contrib import admin
from django.urls import path, include
from .views import insert_data

urlpatterns = [
    path('electricity/solar/insert/content', insert_data, name='insert_data'),
]
