from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from categories.models import Category
from categories.serializers import CategorySerializer

# Create your views here.

@api_view(['GET'])
def categories_with_products_list(request):
    categories = Category.objects.all()
    serialized_data = CategorySerializer(categories, many=True).data
    return Response(serialized_data)