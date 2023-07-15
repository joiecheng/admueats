from django.urls import path

from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("cafs", views.cafs, name="cafs-page"),
    path("cafs/<slug:slug>", views.caf_detail,
         name="caf-detail-page") 
]