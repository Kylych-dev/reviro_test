from rest_framework import serializers
from apps.accounts.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "id",
            "profile",
            "first_name",
            "last_name",
            "role",
        ]




'''
    uid
    role 
    email
    first_name 
    last_name 
    profile 
    is_staff 
    is_active 
    verification_code
    date_joined 
    updated_at 


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()
'''