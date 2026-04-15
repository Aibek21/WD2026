import django_filters

from api.models import Product


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    price_min = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    high_price = django_filters.BooleanFilter(method='filter_high_price')

    class Meta:
        model = Product
        fields = ['name', 'price_min', 'price_max', 'high_price']

    def filter_high_price(self, queryset, name, value):
        if value == True:
            return queryset.filter(price__gt=20000)
        return queryset
