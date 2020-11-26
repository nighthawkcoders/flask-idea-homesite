from django.urls import path
from . import views
#from .views import courses_page

urlpatterns = [
    path('', views.courses_page, name='courses_page'),
    path('python/', views.python_home, name='python_home'),
    path('java/', views.java_home, name='java_home'),
    path('java/repos', views.java_repos, name='java_repos'),
    path('java/timeline', views.java_timeline, name='java_timeline'),
    path('java/guide', views.java_guide, name='java_guide'),
    path('java/ap-standards', views.java_ap, name='java_ap'),

    path('java/roles-in-comp-sci/', views.roles_post, name='roles_post'),
    path('addarticle/', views.sync_article, name='sync_article'),
    path('articles/', views.all_articles, name='all_articles'),
    path('articles/<slug:article>/', views.display_article, name='display_article')

]