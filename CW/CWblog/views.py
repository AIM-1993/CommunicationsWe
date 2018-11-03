from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.conf import settings
import os
# from django.core.cache import cache
# from django.views.decorators.cache import cache_page
# from django_redis import get_redis_connection
from .models import Author, Article


# conn = get_redis_connection("default")
# Create your views here.

# @cache_page(60)
def home(request):
    if request.method == "GET":
        content = {"article" : Article.objects.all(), "Warning": "For testing"}
        return render(request, "CWblog/home.html", content)

# @cache_page(60)
def blog(request):
        return render(request, "CWblog/blog.html")

# @cache_page(60)
def gallery(request):
        return render(request, "CWblog/gallery.html")

# @cache_page(60)
def about(request):
        return render(request, "CWblog/about.html")

# @cache_page(60)
def write_article(request):
    return render(request, "CWblog/write_article.html")
