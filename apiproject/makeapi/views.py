from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
# Create your views here.
@api_view(["GET","POST"])
def get_products_view(request):
    products = Product.objects.all()
    serializer=ProductSerializer(products,many=True)
    return Response(serializer.data)
@api_view()
def get_single_product(request,id):
    return Response(f"Single Product {id}")