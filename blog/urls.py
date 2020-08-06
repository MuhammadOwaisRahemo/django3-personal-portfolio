from . import views
from django.urls import path


urlpatterns = [
    path("", views.index, name="all_blog"),
    path('<int:blog_id>/', views.details, name="detail")
]
