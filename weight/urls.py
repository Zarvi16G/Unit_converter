from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="weight"),
    path("convert_weight/", views.convert_weight, name="convert_weight"),
]