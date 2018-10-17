from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.conf import settings
import os
# from django.core.cache import cache
# from django.views.decorators.cache import cache_page
# from django_redis import get_redis_connection
from .models import Author, Article, Img


# conn = get_redis_connection("default")
# Create your views here.

# @cache_page(60)
def home(request):
    if request.method == "GET":
        content = {"article" : Article.objects.all(), "Warning": "For testing"}
        return render(request, "CWcore/home.html", content)

# @cache_page(60)
def voiceblog(request):
    if request.method == "GET":
        return render(request, "CWcore/voiceblog.html")


# @cache_page(60)
def vlog(request):
    if request.method == "GET":
        return render(request, "CWcore/vlog.html")


# @cache_page(60)
def about(request):
        if request.method == "GET":
            return render(request, "CWcore/about.html")


def uploadimg(request):
    if request.method == 'POST':
        if request.FILES:
            new_img = Img(img=request.FILES.get('img'), name = request.FILES.get('img').name)
            new_img.save()
            return render(request, "CWcore/home.html")
        else:
            return HttpResponseRedirect('/home/', {'warning': "还未选择需要上传的文件！"})
    
    else:
        return render(request, 'CWcore/home.html', {'warning': "还未选择需要上传的文件！"})



			