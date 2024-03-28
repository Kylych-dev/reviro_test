from rest_framework import serializers
from apps.establishment.models import Establishment



class EstablishmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Establishment
        fields = (
            'uuid'
            'name',
            'description',
            'locations',
            'opening_hours',
            'requirements',
            'manager'
        )



'''

    id 
    name 
    description
    locations 
    opening_hours
    requirements


est create only admin

{
    "name": "globus",
    "description": "megamarket",
    "locations": "bishkek",
    "opening_hours": "24/7",
    "requirements": "dresscode"
}


'''