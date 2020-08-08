from django.db import models
from django.utils.text import slugify
from random import randint

class Article(models.Model):

    title = models.CharField(max_length=100, unique=False)
    slug = models.SlugField(max_length=100)
    summary = models.CharField(max_length=300)
    content = models.TextField()
    created = models.DateTimeField()
    updated = models.DateTimeField()
    author = models.CharField(max_length=100)
    date_posted = models.DateTimeField()
    fid = models.IntegerField()

    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):

        slugged_title = slugify(self.title, allow_unicode=True)

        if not slugged_title:
            slugged_title = 'dont-use-emojis'

        post_family = Article.objects.filter(author=self.author)

        similar_posts = post_family.filter(slug=slugged_title)

        i = 10
        while len(similar_posts) > 1:
            slugged_title += str(randint(0, i))
            similar_posts = post_family.filter(slug=slugged_title)
            i *= i

        """
        slug_posts = Post.objects.filter(slug=slugged_title)
        if slug_posts:
            slugged_title += str(len(slug_posts))
        """

        self.slug =  slugged_title

        super(Article, self).save(*args, **kwargs)
