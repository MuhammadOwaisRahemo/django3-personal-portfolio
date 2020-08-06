from . import views
from django.urls import path

urlpatterns = [
    path("", views.Home, name="pg"),
    path("pas/", views.pas, name="password"),
    path("about/", views.about, name="about")
]
