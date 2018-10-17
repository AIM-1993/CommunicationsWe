from django.urls import path
from .import views

app_name = "CWcore"

urlpatterns = [
    path('home/', views.home, name="home"),
    path('upload/', views.uploadimg, name="uploadimg"),
    path('voice/', views.voiceblog, name="voiceblog"),
    path('vlog/', views.vlog, name="vlog"),
    path('about/', views.about, name="about"),
    path('warning/', views.uploadimg),
]