from rest_framework.decorators import api_view
# from django.shortcuts import get_object_or_404
from rest_framework import status
from .serializers import ProductSerializer
from .models import Product
from rest_framework.response import Response
from rest_framework import generics, mixins, permissions, authentication
from authentication.authentication import MyTokenAuthentication

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

    # authentication_classes= [
    #     authentication.SessionAuthentication, 
    #     # authentication.TokenAuthentication,
    #     MyTokenAuthentication, #custom authentication token
    # ]
    # permission_classes = [permissions.IsAuthenticated]
 
    #optional. Used to customize Creation
    def perform_create(self, serializer):
        content= serializer.validated_data.get('content')
        
        if not content:
            content= serializer.validated_data.get('title')
        
        serializer.save(content= content)

    

class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset= Product.objects.all()
    serializer_class= ProductSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'product_id'


    # optional. Used to customize updation
    def perform_update(self, serializer):
        instance= serializer.save()
        
        if not instance.content:
            instance.content = instance.title
            instance.save(update_fields = ['content'])



class ProductDestroyAPIView(generics.DestroyAPIView): 
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    lookup_url_kwarg= 'product_id'



class ProductAddListView(generics.GenericAPIView, mixins.CreateModelMixin):

    serializer_class = ProductSerializer

    def post(self, request, *args, **kwargs):
        serializer= self.get_serializer(data = request.data, many=True)
        
        serializer.is_valid(raise_exception= True)

        self.perform_create(serializer)

        return Response(data= serializer.data, status= status.HTTP_201_CREATED)


# all crud operations combined into one
class ProductNormalCrudView(generics.GenericAPIView,
                            mixins.ListModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.CreateModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin
                            ):
    
    queryset= Product.objects.all()
    serializer_class= ProductSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'product_id'

    # list and detail views
    def get(self, request, *args, **kwargs):
        id = kwargs.get('product_id')

        if id is not None:
            return self.retrieve(request, *args, **kwargs)
        
        return self.list(request, *args, **kwargs)

    # create view
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # update view
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    # delete view
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)