from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from landing.models import *

class HomeSitemap(Sitemap):

    def items(self):
        return ['home']

    def location(self, item):
        return reverse(item)

class ConatctsSitemap(Sitemap):

    def items(self):
        return ['contacts']

    def location(self, item):
        return reverse(item)
