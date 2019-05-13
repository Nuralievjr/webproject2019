from django.http import Http404, JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
import copy
from api.models import Category,Product,ContactModel
from api.serializer import CategorySerializerModel,ProductSerializer,ContactSerializer
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from api.filters import ProductFilter



class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializerModel
    #permission_classes = (IsAuthenticated, )

    #def get_queryset(self):
        #return Category.objects.for_user(self.request.user)

    #def get_serializer_class(self):
        #return CategorySerializerModel

    #def perform_create(self, serializer):
        #serializer.save(created_by=self.request.user)


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializerModel


class CategoryProductList(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    #pagination_class = LimitOffsetPagination
    #filter_backends = (DjangoFilterBackend,
                       #filters.SearchFilter,
                       #filters.OrderingFilter)

    # TODO DjangoFilterBackend
    #filter_class = ProductFilter
    # filterset_fields = ('name', 'price')

    # TODO SearchFilter
    #search_fields = ('name', 'price', 'count')

    # TODO OrderingFilter
    #ordering_fields = ('-count',)

    #ordering = ('price',)

    def get_queryset(self):
        # category = get_object_or_404(Category, id=self.kwargs.get('pk'))
        try:
            category = Category.objects.get(id=self.kwargs.get('pk'))
        except Category.DoesNotExist:
            raise Http404
        queryset = category.product_set.all()

        # TODO Query params
        # name = self.request.query_params.get('name', None)
        # price = self.request.query_params.get('price', None)
        # if name is not None and price is not None:
        #     queryset = queryset.filter(name=name).filter(price=price)

        return queryset


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


@api_view(['PUT'])
def putLike(request, pk):
    if request.method == 'PUT':
        try:
            product = Product.objects.get(id=pk)
        except Product.DoesNotExist as e:
            raise Response(status = status.HTTP_404_NOT_FOUND)
        product.visit += 1
        product.save()
        return Response(status=status.HTTP_200_OK)
    return Response({"error":"bad request"})



class Products(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend,)
    #filterset_fields = ('name',)
    filter_class = ProductFilter




class ProductsPopular(generics.ListAPIView):
    serializer_class = ProductSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering = ('-visit',)
    queryset = Product.objects.all()


    queryset = queryset.filter(visit__gte=10)




class Contact(generics.CreateAPIView):
    queryset = ContactModel.objects.all()
    serializer_class = ContactSerializer





