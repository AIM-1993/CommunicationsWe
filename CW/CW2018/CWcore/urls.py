from django.urls import path
from . import views

app_name = "CWcore"

urlpatterns = [
    path('', views.index, name="index")
]