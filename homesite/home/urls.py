from django.contrib import admin
from django.urls import path
from .views import home_page, about_page

urlpatterns = [
    path('', home_page, name='home_page'),
    path('about/', about_page, name='about_page'),

]