from rest_framework.generics import ListAPIView
from .serializers import *
from .models import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination

class ProductPagination(LimitOffsetPagination):
    default_limit=10
    max_limit=20
class ProductList(ListAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    filter_backends=(DjangoFilterBackend,SearchFilter)
    filter_fields=('id',)
    search_fields=('product_name','product_price')
    pagination_class=ProductPagination