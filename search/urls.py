from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.get_json_from_query),
    path("(<str:keyword>", views.get_json_from_query),
    path("home/", views.home),
    path("about/", views.about),

]