from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="blogIndex"),
    path("blogpost/<int:myid>/", views.blogpost, name="blogPost")
]
