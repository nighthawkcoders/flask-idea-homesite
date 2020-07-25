from django.shortcuts import render

def courses_page(request):
    return render(request, 'courses/courses.html')


def roles_post(request):
    return render(request, 'courses/java/roles_post.html')