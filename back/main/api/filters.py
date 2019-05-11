from django_filters import rest_framework as filters
from api.models import Product


class ProductFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='istartswith')

    class Meta:
        model = Product
        fields = ('name',)
