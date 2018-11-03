from django.urls import path
from .views import HomeView, BlogView, GalleryView, AboutView, Write_ArticleView, BooksView

app_name = 'CWblog'

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('blog/', BlogView.as_view(), name="blog"),
    path('gallery/', GalleryView.as_view(), name="gallery"),
    path('about/', AboutView.as_view(), name="about"),
    path('write_Article/', Write_ArticleView.as_view(), name="write_article"),
    path('booksview/', BooksView.as_view(), name="books"),
]
