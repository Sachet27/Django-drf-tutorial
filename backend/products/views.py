from rest_framework.decorators import api_view
# from django.shortcuts import get_object_or_404
from rest_framework import status
from .serializers import ProductSerializer
from .models import Product
from rest_framework.response import Response
from rest_framework import generics


# @api_view(['GET'])
# def product_list(request):
#     products= Product.objects.all() 
#     serializer= ProductSerializer(products, many= True)

#     return Response(serializer.data)

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class= ProductSerializer


# @api_view(['GET'])
# def details(request, product_id):
#     try:
#         product= Product.objects.get(id= product_id)
#     except Product.DoesNotExist:
#         return Response(
#             data= {'error': 'Product does not exist.'},
#             status= status.HTTP_404_NOT_FOUND
#         )

#     # product= get_object_or_404(Product, id= product_id)

#     serializer= ProductSerializer(instance= product)
#     return Response(serializer.data)



class ProductRetrieveAPIView(generics.RetrieveAPIView):
    queryset= Product.objects.all()
    serializer_class= ProductSerializer
    lookup_field= 'pk' #directly defaults to the primary key. If not specified, then id use garxa
    lookup_url_kwarg= 'product_id'


# @api_view(['POST'])
# def create(request):
#     product= request.data

#     serializer= ProductSerializer(data= product)

#     if serializer.is_valid():
#         serializer.save()
#         return Response(data= serializer.data, status= status.HTTP_201_CREATED)

#     return Response(
#         data= {'errors': serializer.errors},
#         status= status.HTTP_400_BAD_REQUEST
#     )

class ProductCreateAPIView(generics.CreateAPIView):
    # queryset = Product.objects.all()
    serializer_class= ProductSerializer
    






