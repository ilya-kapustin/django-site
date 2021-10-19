from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewsSitemap(Sitemap):
    def items(self):
        return ['about', 'contacts']

    def location(self, item):
        return reverse(item)
