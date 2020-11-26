from flask import render_template

from __init__ import app

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/about')
def contacts():
    return render_template("contact.html")

"""
def about_page(request):
    return render(request, 'home/about.html')

def product_page(request):
    return render(request, 'home/products.html')

def courses_page(request):
    return render(request, 'home/courses.html')


from django.urls import path, include
from views import home_page, about_page, product_page, donate_page

urlpatterns = [
    path('', home_page, name='home_page'),
    path('about/', about_page, name='about_page'),
    path('products/', product_page, name='product_page'),
    path('donate/', donate_page, name='donate_page'),
    path('courses/', include('courses.urls')),
]
"""