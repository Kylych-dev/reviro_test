from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from apps.accounts.models import CustomUser


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    role = serializers.CharField()
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    print(role, '*****************************************')

    class Meta:
        model = CustomUser
        fields = (
            "email",
            "role",
            "password",
            "password2",

        )
        extra_kwargs = {
            "password": {"write_only": True},
            # "first_name": {"required": True},
            # "last_name": {"required": True},
        }

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})
        return attrs
