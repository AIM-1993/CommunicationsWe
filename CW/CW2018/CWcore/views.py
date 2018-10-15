from django.shortcuts import render
from django.http import Http404
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django_redis import get_redis_connection
from .models import Author, Article


conn = get_redis_connection("default")
# Create your views here.

@cache_page(60 * 15)
def home(request):
    if request.method == "GET":
        content = {"article" : Article.objects.all(), "Warning": "For testing"}
        return render(request, "CWcore/home.html", content)


@cache_page(60 * 15)
def about(request):
        if request.method == "GET":
                return render(request, "CWcore/about.html")


