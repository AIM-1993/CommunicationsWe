from django.urls import path
from .views import homeView, blogView, galleryView, aboutView, write_articleView

app_name = 'CWblog'

urlpatterns = [
    path('', homeView.as_view(), name="home"),
    path('blog/', blogView.as_view(), name="blog"),
    path('gallery/', galleryView.as_view(), name="gallery"),
    path('about/', aboutView.as_view(), name="about"),
    path('write_article/', write_articleView.as_view(), name="write_article"),
]
