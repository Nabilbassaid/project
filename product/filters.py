import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')
    key = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    min_price = django_filters.NumberFilter(field_name='price' or 0, lookup_expr='lte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')


    class Meta:
        model = Product
        fields = ['brand', 'category','id','key','min_price','max_price']