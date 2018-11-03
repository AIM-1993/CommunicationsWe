from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.conf import settings
from django.views import View
import os
# from django.core.cache import cache
# from django.views.decorators.cache import cache_page
# from django_redis import get_redis_connection
from .models import Author, Article


# conn = get_redis_connection("default")
# Create your views here.

# @cache_page(60)
class homeView(View):
    def get(self, request):
        if request.method == "GET":
            content = {"article" : Article.objects.all(), "Warning": "For testing"}
            return render(request, "CWblog/home.html", content)

class blogView(View):
    def get(self, request):
        return render(request, "CWblog/blog.html")

# @cache_page(60)
class galleryView(View):
    def get(self, request):
        return render(request, "CWblog/gallery.html")

# @cache_page(60)
class aboutView(View):
    def get(self, request):
        return render(request, "CWblog/about.html")

# @cache_page(60)
class write_articleView(View):
    def get(self, request):
        return render(request, "CWblog/write_article.html")
