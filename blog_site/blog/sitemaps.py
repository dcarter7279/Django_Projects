from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from taggit.models import Tag

class TagSitemap(Sitemap):
    priority = 0.9
    changefreq = 'weekly'
    def items(self):
        return Tag.objects.all()
    def location(self, item):
        return reverse('blog:post_list_by_tag', args=[item.slug])