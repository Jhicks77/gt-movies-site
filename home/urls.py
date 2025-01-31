from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    path("", views.index, name="home.index"),
    path("about", views.about, name="home.about"),
]