from django.http import Http404, JsonResponse
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
import copy
from api.models import Category,Product
from api.serializer import CategorySerializerModel,ProductSerializer


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
    #ordering_fields = ('name', 'price')

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

class Products(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductsPopular(generics.ListAPIView):
    queryset = Product.objects.all()
    queryset = queryset.filter(visit__gte=0)
    serializer_class = ProductSerializer






