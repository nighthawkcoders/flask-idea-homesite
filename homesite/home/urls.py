from django.contrib import admin
from django.urls import path, include
from .views import home_page, about_page, product_page, donate_page, courses_page

urlpatterns = [
    path('', home_page, name='home_page'),
    path('about/', about_page, name='about_page'),
    path('products/', product_page, name='product_page'),
    path('donate/', donate_page, name='donate_page'),
    path('courses/', include('courses.urls')),
]