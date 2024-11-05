from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="length"),
    path("convert_length/", views.convert_length, name="convert_length"),
]