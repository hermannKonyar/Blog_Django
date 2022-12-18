from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name='home'),
    path("main", views.index),
    path("blogs", views.blogs, name='blogs'),
    path("blogs/<int:id>", views.blog_details, name='blog_details'),
    # path("tarifler",views.tarifler,name="tarifler"),
    # path("tarifler/<int:id>", views.tarifler_details, name='tarifler_details'),
    path("hakkimda",views.hakkimda,name="hakkimda"),

]
