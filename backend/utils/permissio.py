from rest_framework import permissions
from django.utils import timezone
from datetime import datetime, timedelta


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Разрешить чтение всем пользователям
        if request.method in permissions.SAFE_METHODS:
            return True
        # Разрешить запись только владельцу объекта
        return obj.user == request.user


class IsManagerOrReadOnly(permissions.BasePermission):
    '''
    Разрешает чтение всем пользователям,
    но позволяет обновление, создание и 
    удаление только владельцам.
    '''

    def has_permission(self, request, view):
        # Разрешить чтение всем пользователям
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Для остальных методов проверяем, является ли пользователь менеджером
        return request.user and request.user.role == 'manager'
