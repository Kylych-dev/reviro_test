from rest_framework import serializers
from apps.product.models import Product



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ( 
            'uuid',
            'name',
            'description', 
            'price', 
            'quantity_in_stock',
            'production_date',
            'expiration_date',
            'availability_status',
            'establishment'

        )



'''
prod create manager

{
  "name": "bounty",
  "description": "batonchik",
  "price": 5.99,
  "quantity_in_stock": 10,
  "production_date": "2024-03-31",
  "expiration_date": "2024-04-30",
  "establishment": "17630f08-37bc-4ef5-ae6d-d5f8b9c4e7f2"
}

    id 
    name 
    description 
    price 
    quantity_in_stock 

    establishment
    'production_date',
    'expiration_date',
    'establishment'


'''