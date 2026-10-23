
from django.urls import path
from . import views

urlpatterns = [
    path("hello/", views.hello, name="hello"),
    path("shorten/", views.shorten_url, name="shorten_url"),
]
