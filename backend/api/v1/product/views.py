from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status, permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from apps.product.models import Product
from .serializers import ProductSerializer
from utils.customer_logger import log_error, log_warning
from utils.permissio import IsManagerOrReadOnly




class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated, IsManagerOrReadOnly]
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['availability_status']
    search_fields = ['name']
    lookup_field = 'pk'

    @swagger_auto_schema(
        method="get",
        operation_description="Получить список продуктов",
        operation_summary="Получение списка продуктов",
        operation_id="list_products",
        tags=["Product"],
        responses={
            200: openapi.Response(description="OK - Список успешно получен"),
            400: openapi.Response(description="Bad Request - Неверный запрос"),
            401: openapi.Response(description="Unauthorized - Неавторизованный запрос"),
            404: openapi.Response(description="Not Found - Ресурс не найден"),
        },
    )
    @action(detail=False, method=["get"])
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())  # Применяем фильтры, если они заданы
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        method="put",
        operation_description="Обновление данных продукта",
        operation_summary="Обновление данных продукта",
        operation_id="update_products",
        tags=["Product"],
        responses={
            200: openapi.Response(description="OK - Продукт успешно обновлен"),
            400: openapi.Response(description="Bad Request - Неверный запрос или некорректные данные"),
            401: openapi.Response(description="Unauthorized - Неавторизованный запрос"),
            404: openapi.Response(description="Not Found - Ресурс не найден"),
        },
    )
    @action(detail=True, methods=["put"])
    def update(self, request, *args, **kwargs):
        try:
            product = self.get_object()
            serializer = ProductSerializer(product, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    serializer.data, 
                    status=status.HTTP_200_OK
                    )
            log_error(self, ex)
            return Response(
                serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST
                )
        except Exception as ex:
            log_warning(self, ex)
            return Response(
                {"Сообщение": str(ex)}, 
                status=status.HTTP_404_NOT_FOUND
                )

    @swagger_auto_schema(
        method="post",
        operation_description="Создание продуктов",
        operation_summary="Создание продуктов",
        operation_id="create_product",
        tags=["Product"],
        responses={
            201: openapi.Response(description="Created - Новый продукт успешно создан"),
            400: openapi.Response(description="Bad Request - Неверный запрос"),
            401: openapi.Response(description="Unauthorized - Неавторизованный запрос"),
            404: openapi.Response(description="Not Found - Ресурс не найден"),
        },
    )
    @action(detail=True, methods=["post"])
    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as ex:
            log_error(self, ex)
            return Response(
                {"Сообщение": str(ex)}, 
                status=status.HTTP_400_BAD_REQUEST
                )


    @swagger_auto_schema(
        method="delete",
        operation_description="Удаление продукта",
        operation_summary="Удаление продукта",
        operation_id="delete_product",
        tags=["Product"],
        responses={
            204: openapi.Response(description="No Content - Продукт успешно удален"),
            401: openapi.Response(description="Unauthorized - Неавторизованный запрос"),
            404: openapi.Response(description="Not Found - Продукт не найден"),
        },
    )
    @action(detail=True, methods=["delete"])
    def delete(self, request, *args, **kwargs):
        try:
            print(self.get_object(), '<---------------------------------------')
            instance = self.get_object()
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as ex:
            log_warning(self, ex)
            return Response(
                {"Сообщение": str(ex)}, 
                status=status.HTTP_404_NOT_FOUND
                )