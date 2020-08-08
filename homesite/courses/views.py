from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.views.decorators.csrf import csrf_exempt
from .models import Article
from dateutil.parser import parse
import requests
import hashlib

def courses_page(request):
    return render(request, 'courses/courses.html')


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
            
            article = Article(title=rj['title'], 
            slug=rj['slug'], 
            summary=rj['summary'], 
            content=rj['content'], 
            created=parse(rj['created']), 
            updated=parse(rj['updated']), 
            author=(rj['author_firstname']+" "+rj['author_lastname']), 
            date_posted=parse(rj['date_posted']))

            article.save()


            return HttpResponse({'YAAYY':'made it!'}, content_type="application/json")


    raise Http404("Page not found")

def pbl_post(request):

    response = requests.get(r'http://167.99.167.145/sarika/project-based-learning/json')

    return render(request, 'courses/pbl.html', response.json())