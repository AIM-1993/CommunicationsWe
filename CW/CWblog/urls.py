from django.urls import path
from .import views

app_name = "CWblog"

urlpatterns = [
    path('', views.home, name="home"),
    path('blog/', views.blog, name="blog"),
    path('gallery/', views.gallery, name="gallery"),
    path('about/', views.about, name="about"),
]
