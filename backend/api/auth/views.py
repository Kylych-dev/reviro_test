from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework_simplejwt.exceptions import AuthenticationFailed, TokenError
from rest_framework import status, viewsets, permissions, views
from rest_framework_simplejwt.settings import api_settings
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from datetime import datetime


from .serializers import RegisterSerializer
from apps.accounts.models import CustomUser
from utils.customer_logger import log_error



class RegisterView(viewsets.ViewSet):
    serializer_class = RegisterSerializer

    @swagger_auto_schema(
        operation_description="Создание нового пользователя.",
        operation_summary="Создание нового пользователя",
        operation_id="register_user",
        tags=["Authentication"],
        responses={
            201: openapi.Response(description="OK - Регистрация прошла успешно."),
            400: openapi.Response(description="Bad Request - Неверный запрос."),
        },
    )
    def register(self, request, *args, **kwargs):
        print(request.data, '<<<<<<<<<<<<_______________________')
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                validated_data = serializer.validated_data
                email = validated_data.get("email")
                validated_data.pop("password2")

                # Проверяем наличие пользователя
                existing_user = CustomUser.objects.filter(email=email).exists()
                if existing_user:
                    return Response(
                        data={"error": "Пользователь с таким email уже существует"},
                        status=status.HTTP_400_BAD_REQUEST
                    )
                role = validated_data.get('role')
                user = CustomUser.objects.create_user(
                    email=email, 
                    role=role, 
                    password=validated_data.get("password")
                    )
                user.set_password(validated_data.get("password"))
                user.save()
                return Response(
                    serializer.data, 
                    status=status.HTTP_201_CREATED
                    )
            except Exception as ex:
                log_error(self, ex)
                return Response(
                    data={"error": f"User creation failed: {str(ex)}"},
                    status=status.HTTP_400_BAD_REQUEST,)
        else:
            log_error(self, ex)
            return Response(
                serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST
                )


class UserAuthenticationView(viewsets.ViewSet):

    @swagger_auto_schema(
        operation_description="Авторизация пользователя для получения токена.",
        operation_summary="Авторизация пользователя для получения токена",
        operation_id="login_user",
        tags=["Authentication"],
        responses={
            200: openapi.Response(description="OK - Авторизация пользователя прошла успешно."),
            400: openapi.Response(description="Bad Request - Неверный запрос."),
            404: openapi.Response(description="Not Found - Пользователь не найден"),
        },
    )
    def login(self, request):
        email = request.data["email"]
        password = request.data["password"]
        try:
            user = CustomUser.objects.get(email=email)

        except CustomUser.DoesNotExist:
            raise AuthenticationFailed("Такого пользователя не существует")

        if user is None:
            raise AuthenticationFailed("Такого пользователя не существует")

        if not user.check_password(password):
            raise AuthenticationFailed("Не правильный пароль")

        access_token = AccessToken.for_user(user)
        refresh_token = RefreshToken.for_user(user)

        # ___________________________________________________________
        # Допольнительная ифнормация о токене
        access_token_lifetime = api_settings.ACCESS_TOKEN_LIFETIME
        refresh_token_lifetime = api_settings.REFRESH_TOKEN_LIFETIME
        current_datetime = datetime.now()
        access_token_expiration = current_datetime + access_token_lifetime
        refresh_token_expiration = current_datetime + refresh_token_lifetime
        # ___________________________________________________________

        return Response(
            data={
                "access_token": str(access_token),
                "access_token_expires": access_token_expiration.strftime("%Y-%m-%d %H:%M:%S"),

                "refresh_token": str(refresh_token),
                "refresh_token_expires": refresh_token_expiration.strftime("%Y-%m-%d %H:%M:%S"),
                
                "email": user.email,
                "role": user.role,
            },
            status=status.HTTP_200_OK,
        )

    @swagger_auto_schema(
        operation_description="Выход для удаления токена.",
        operation_summary="Выход для удаления токена",
        operation_id="logout_user",
        tags=["Authentication"],
        responses={
            201: openapi.Response(description="OK - Выход пользователя прошла успешно."),
            400: openapi.Response(description="Bad Request - Неверный запрос."),
        },
    )
    def logout(self, request):
        try:
            if "refresh_token" in request.data:
                refresh_token = request.data["refresh_token"]
                if refresh_token:
                    token = RefreshToken(refresh_token)
                    token.blacklist()
                return Response("Вы вышли из учетной записи", 
                                status=status.HTTP_200_OK
                                )
            else:
                return Response(
                    "Отсутствует refresh_token", 
                    status=status.HTTP_400_BAD_REQUEST
                )
        except TokenError:
            raise AuthenticationFailed("Не правильный токен")
