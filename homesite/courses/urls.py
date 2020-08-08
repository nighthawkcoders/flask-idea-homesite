from django.contrib import admin
from django.urls import path, include
from . import views
#from .views import courses_page

urlpatterns = [
    path('', views.courses_page, name='courses_page'),
    path('java/roles-in-comp-sci/', views.roles_post, name='roles_post'),
    path('addarticle/', views.sync_article, name='sync_article'),
    path('<slug:article>/', views.display_article, name='display-article')

]