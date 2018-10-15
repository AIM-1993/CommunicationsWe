from django.shortcuts import render
from django.http import Http404
from .models import Author, Article

# Create your views here.
def home(request):
    if request.method == "GET":
        content = {"article" : Article.objects.all(), "Warning": "For testing"}
        return render(request, "CWcore/home.html", content)


def about(request):
        if request.method == "GET":
                return render(request, "CWcore/about.html")


