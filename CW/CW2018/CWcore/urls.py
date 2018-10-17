from django.urls import path
from .import views

app_name = "CWcore"

urlpatterns = [
    path('home/', views.home, name="home"),
    path(r'^upload$', views.uploadimg, name="uploadimg"),
    path('voice/', views.voiceblog, name="voiceblog"),
    path('vlog/', views.vlog, name="vlog"),
    path('about/', views.about, name="about"),
]