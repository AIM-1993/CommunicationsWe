from django.contrib import admin
from .models import Author, Article, Gallery
# Register your models here.
admin.site.register(Author)
admin.site.register(Article)
admin.site.register(Gallery)