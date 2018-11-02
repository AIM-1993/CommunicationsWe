from django.urls import path
from .import views

app_name = "CWblog"

urlpatterns = [
    path('', views.home, name="home"),
    path('voice/', views.voiceblog, name="voiceblog"),
    path('vlog/', views.vlog, name="vlog"),
    path('about/', views.about, name="about"),
]