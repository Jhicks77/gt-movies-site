from django.urls import path, include
from . import views

app_name = "polls"
urlpatterns = [
    path("", views.test_view, name="test"),
]