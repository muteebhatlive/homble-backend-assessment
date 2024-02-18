from django.urls import path

from .views import *

urlpatterns = [
    path("", products_list, name="products-list"),
    path("create-sku/", create_sku, name="create-sku"),
    path("info/<int:pk>", product_info, name="product-info"),
    path('edit-sku/<int:sku_id>', edit_sku_status, name='edit_sku_status'),
    
]
