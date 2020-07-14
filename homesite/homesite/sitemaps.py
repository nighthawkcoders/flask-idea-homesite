from django.contrib import sitemaps
from django.urls import reverse

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['home_page', 'about_page', 'product_page', 'donate_page', 'courses_page']

    def location(self, item):
        return reverse(item)