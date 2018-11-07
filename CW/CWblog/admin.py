from django.contrib import admin
from .models import Author, Article, Userupdate, Gallery
# Register your models here.
admin.site.register(Author)
admin.site.register(Article)
admin.site.register(Userupdate)
admin.site.register(Gallery)