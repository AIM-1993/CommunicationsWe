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
def voiceblog(request):
    if request.method == "GET":
        return render(request, "CWblog/voiceblog.html")


# @cache_page(60)
def vlog(request):
    if request.method == "GET":
        return render(request, "CWblog/vlog.html")


# @cache_page(60)
def about(request):
        if request.method == "GET":
            return render(request, "CWblog/about.html")




			