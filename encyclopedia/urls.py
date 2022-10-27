from django.urls import include,path

from markdown2 import markdown

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.displayEntry, name="showEntry"),
    path("search/", views.search, name="search"),
    path("newPage/", views.newPage, name="newPage"),
    path("editPage/", views.editPage, name="editPage"),
    path("randomPage/", views.randomPage, name='randomPage')
]
