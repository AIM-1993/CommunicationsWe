from django.shortcuts import render
from django.views import View
# from django.core.cache import cache
# from django.views.decorators.cache import cache_page
# from django_redis import get_redis_connection
from .models import Article, Gallery
# conn = get_redis_connection("default")
# Create your views here.

# @cache_page(60)
class HomeView(View):
    def get(self, request):
        if request.method == "GET":
            content = {"article" : Article.objects.all()}
            return render(request, "CWblog/home.html", content)

# @cache_page(60)
class BlogView(View):
    def get(self, request):
        return render(request, "CWblog/blog.html")

# @cache_page(60)
class GalleryView(View):
    def get(self, request):
        if request.method == "GET":
            imgs = Gallery.objects.all()
            content = {"imgs" : imgs}
            return render(request, "CWblog/gallery.html", content)

# @cache_page(60)
class AboutView(View):
    def get(self, request):
        return render(request, "CWblog/about.html")

# @cache_page(60)
class Write_ArticleView(View):
    def get(self, request):
        return render(request, "CWblog/write_article.html")

# @cache_page(60)
class BooksView(View):
    def get(self, request):
        return render(request, "CWblog/books.html")
