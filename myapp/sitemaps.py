from django.contrib.sitemaps import Sitemap
from .models import Project
from django.urls import reverse

class ProjectSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return Project.objects.all()

    def lastmod(self, obj):
        return obj.updated_at

class StaticViewSitemap(Sitemap):
    priority = 0.6
    changefreq = 'monthly'

    def items(self):
        return ['index', 'contact', 'projects']

    def location(self, item):
        return reverse(item)
