from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="temperature"),
    path("convert_temperature/", views.convert_temperature, name="convert_temperature"),
]