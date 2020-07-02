from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return render(request, 'home/home.html')

def about_page(request):
    return render(request, 'home/about.html')

def product_page(request):
    return render(request, 'home/products.html')

def donate_page(request):
    return render(request, 'home/donate.html')