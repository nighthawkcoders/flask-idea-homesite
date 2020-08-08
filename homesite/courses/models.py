from django.db import models

class Article(models.Model):

    title = models.CharField(max_length=100, unique=False)
    slug = models.SlugField(max_length=100)
    summary = models.CharField(max_length=300)
    content = models.TextField()
    created = models.DateTimeField()
    updated = models.DateTimeField()
    author = models.CharField(max_length=100)
    date_posted = models.DateTimeField()

    def __str__(self):
        return self.title