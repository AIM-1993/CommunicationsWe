from django.urls import path, re_path
from .views import HomeView, BlogView, GalleryView, DetailView, AboutView, Write_ArticleView, BooksView

app_name = 'CWblog'

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('blog/', BlogView.as_view(), name="blog"),
    re_path(r'^detail/(?P<pk>[0-9]+)/$', DetailView.as_view(), name="detail"),
    path('gallery/', GalleryView.as_view(), name="gallery"),
    path('about/', AboutView.as_view(), name="about"),
    path('write_Article/', Write_ArticleView.as_view(), name="write_article"),
    path('booksview/', BooksView.as_view(), name="books"),
]
