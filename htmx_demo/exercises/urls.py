"""URL configuration for the exercises app."""

from django.urls import path

from . import views

app_name = "exercises"

urlpatterns = [
    path("", views.index, name="index"),
    path("<slug:slug>/", views.detail, name="detail"),
]

