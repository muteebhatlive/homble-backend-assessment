from django.urls import path

from .views import *

urlpatterns = [
    path("", categories_with_products_list, name="categories_with_products_list"),
]
