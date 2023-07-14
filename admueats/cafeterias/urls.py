from django.urls import path

from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("cafeterias", views.cafeterias, name="cafeterias-page"),
    path("cafeterias/<slug:slug>", views.caf_detail,
         name="cafeteria-detail-page")  # /products/my-first-product
]
