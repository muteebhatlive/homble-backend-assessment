from django.urls import path

from .views import *

urlpatterns = [
    path("", products_list, name="products-list"), #get all product list 
    path("create-sku/", create_sku, name="create-sku"), #create sku
    path("info/<int:pk>", product_info, name="product-info"), # get details about a product
    path('edit-sku/<int:sku_id>', edit_sku_status, name='edit_sku_status'), # edit sku status
    path('q1', active_categories_with_approved_skus, name=''),
    path('q2', all_skus, name=''),
    
]
