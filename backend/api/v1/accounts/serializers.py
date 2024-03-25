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
            "phone_number",
            "sewing_workshop",
            "employment_status",
        ]
