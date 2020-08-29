from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.views.decorators.csrf import csrf_exempt
from .models import Article
from dateutil.parser import parse
import requests
import hashlib

def courses_page(request):
    return render(request, 'courses/courses.html')


def python_home(request):
    return render(request, 'courses/python/python_home.html')

def java_home(request):
    return render(request, 'courses/java/java_home.html')


# Only Post that is made statically as opposed to an object
def roles_post(request):
    return render(request, 'courses/java/roles_post.html')




@csrf_exempt
def sync_article(request):

    if request.POST.get('iam'):
        print(request.POST.get('iam'))
        result = hashlib.md5(request.POST.get('iam').encode())
        if result.hexdigest() == 'f6c2cfbb0b0eaf5e8e54acc79d0ad5be':
            #verified user

            site = request.POST.get('site') + '/json'
            rj  = requests.get(site).json()
            
            article = Article.objects.filter(fid=rj['id'])

            if article:
                article = article.first()
            else:
                article = Article()

            article.title=rj['title']
            article.summary=rj['summary']
            article.content=rj['content']
            article.created=parse(rj['created'])
            article.updated=parse(rj['updated'])
            article.author=(rj['author_firstname']+" "+rj['author_lastname'])
            article.date_posted=parse(rj['date_posted'])
            article.fid=rj['id']

            article.save()


            return HttpResponse({'status':'success!'}, content_type="application/json")


    raise Http404("Page not found")



def all_articles(request):
    articles = Article.objects.all()
    return render(request, 'courses/all_articles.html', {'articles':articles})

def display_article(request, article):
    article = get_object_or_404(Article, slug=article)
    return render(request, 'courses/display_article.html', {'article':article})