from django.urls import include,path

from markdown2 import markdown

from . import views
from . import util

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.displayEntry, name="showEntry"),
]
