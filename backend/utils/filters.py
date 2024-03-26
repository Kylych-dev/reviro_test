from django_filters import rest_framework as filters
from apps.product.models import Product

class BeverageFilter(filters.FilterSet):
    available = filters.BooleanFilter(field_name='availability_status')

    class Meta:
        model = Product
        fields = ['availability_status']