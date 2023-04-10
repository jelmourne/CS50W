from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create, name="create"),
    path("wiki/<str:wiki_entry>", views.entry, name="entry"),
    path("random", views.rand, name="rand"),
    path("search", views.search, name="search"),
    path("error" , views.errorType, name="errorType"),
    path("wiki/<str:wiki_entry>/edit", views.edit, name="edit")
]
