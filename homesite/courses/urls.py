from django.contrib import admin
from django.urls import path, include
from .views import courses_page

urlpatterns = [
    path('', courses_page, name='courses_page'),
]