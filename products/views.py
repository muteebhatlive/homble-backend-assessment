from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
)
from categories.models import *

from django.shortcuts import get_object_or_404

from .models import *
from .serializers import *



@api_view(["GET"])
@permission_classes([AllowAny])
def products_list(request):
    """
    List of all products.
    """
    refrigerated = request.query_params.get('refrigerated')  # get "refrigerated" query parameter from the request

    if refrigerated is not None:
        products = Product.objects.filter(is_refrigerated=bool(refrigerated))
    else:
        products = Product.objects.all()
    serializer = ProductListSerializer(products, many=True)
    return Response({"products": serializer.data}, status=HTTP_200_OK)


@api_view(['POST'])
def create_sku(request):
    serializer = SkuCreateSerializer(data=request.data)
    print(request.data)
    if serializer.is_valid():
        serializer.save() 
        return Response(serializer.data, status=HTTP_201_CREATED)
    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([AllowAny])
def product_info(request, pk):
    try:
        product = Product.objects.get(pk=pk)     # check for product object
    except Product.DoesNotExist:
        return Response({"message": "Product does not exist"}, status=HTTP_404_NOT_FOUND)

    product_serializer = ProductListSerializer(product)

    
    approved_skus = Sku.objects.filter(product=product, status=1)       # Get all approved Skus for the product
    sku_serializer = SkuCreateSerializer(approved_skus, many=True)

   
    product_serializer_data = product_serializer.data      # Nest into product data
    product_serializer_data['approved_skus'] = sku_serializer.data

    return Response(product_serializer_data)
   
   
   
@api_view(['PUT'])
@permission_classes([IsAdminUser])
def edit_sku_status(request, sku_id):
    sku = get_object_or_404(Sku, pk=sku_id)  #check for obejct 
    
    serializer = SkuEditStatusSerializer(sku, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message": "Sku status updated successfully",
            "data": serializer.data},
            status=HTTP_200_OK)
    else:
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    


@api_view(['GET'])
@permission_classes([AllowAny])

def active_categories_with_approved_skus(request):
    active_categories = Category.objects.filter(is_active=True) # Get all active categories
    # Print each category along with the count of its approved SKUs
    for category in active_categories:
        approved_skus_count = category.products.filter(sku__status=1).count()  # filter and count objects with status = 1
        print(f"Category: {category.name} | Approved SKUs: {approved_skus_count}")
    
    
@api_view(['GET'])
@permission_classes([AllowAny])
def all_skus(request):
    all_skus_with_categories = Sku.objects.select_related('product__category')

    for sku in all_skus_with_categories: # Print each Sku along with its category
        print(f"Sku: {sku} | Category: {sku.product.category.name}")
        
    
    """
    
    Minimal DB queries and minimal python iteration can be achieved using annotation and aggregation.
    
    """