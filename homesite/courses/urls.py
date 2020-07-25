from django.contrib import admin
from django.urls import path, include
from . import views
#from .views import courses_page

urlpatterns = [
    path('', views.courses_page, name='courses_page'),
    path('java/roles-in-comp-sci/', views.roles_post, name='roles_post'),

]