from django.urls import path

from . import views

# this is a URLconf

urlpatterns = [
    path("", views.index, name="index"),
]