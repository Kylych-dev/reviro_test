import pytest
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from apps.product.models import Product, Establishment
from apps.accounts.models import CustomUser

client = APIClient()

@pytest.fixture
def test_user():
    user = CustomUser.objects.create(
        email='testuser@example.com', 
        role='manager', 
        is_superuser=False, 
        is_staff=True
        )
    return user

@pytest.mark.django_db
def test_create_product(test_user):
    establishment = Establishment.objects.create(
        name="Test Establishment", 
        description="qwerty", 
        locations="milan", 
        opening_hours="10", 
        requirements="qewrty",
        manager=test_user
    )
    client.force_authenticate(user=test_user)
    url = reverse("product-create")
    data = {
        "name": "Test Product",
        "description": "Test Description",
        "price": 10.99,
        "quantity_in_stock": 100,
        "availability_status": True,
        "production_date": "2023-01-01",
        "expiration_date": "2024-01-01",
        "category": "Test Category",
        "manufacturer": "Test Manufacturer",
        "establishment": establishment.id
    }
    response = client.post(url, data, format="json")
    assert response.status_code == status.HTTP_201_CREATED

@pytest.mark.django_db
def test_update_product(test_user):
    establishment = Establishment.objects.create(
        name="Test Establishment", 
        description="qwerty", 
        locations="milan", 
        opening_hours="10", 
        requirements="qewrty",
        manager=test_user
    )
    product = Product.objects.create(
        name="Test Product",
        description="Test Description",
        price=10.99,
        quantity_in_stock=100,
        availability_status=True,
        production_date="2023-01-01",
        expiration_date="2024-01-01",
        category="Test Category",
        manufacturer="Test Manufacturer",
        establishment=establishment
    )
    client.force_authenticate(user=test_user)
    url = reverse("product-update", kwargs={"pk": product.pk})
    data = {
        "name": "Updated Test Product",
        "description": "Updated Test Description",
        "price": 19.99,
        "quantity_in_stock": 200,
        "availability_status": False,
        "production_date": "2023-01-01",
        "expiration_date": "2024-01-01",
        "category": "Updated Test Category",
        "manufacturer": "Updated Test Manufacturer",
        "establishment": establishment.id
    }
    response = client.put(url, data, format="json")
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_delete_product(test_user):
    establishment = Establishment.objects.create(
        name="Test Establishment", 
        description="qwerty", 
        locations="milan", 
        opening_hours="10", 
        requirements="qewrty",
        manager=test_user
    )
    product = Product.objects.create(
        name="Test Product",
        description="Test Description",
        price=10.99,
        quantity_in_stock=100,
        availability_status=True,
        production_date="2023-01-01",
        expiration_date="2024-01-01",
        category="Test Category",
        manufacturer="Test Manufacturer",
        establishment=establishment
    )
    client.force_authenticate(user=test_user)
    url = reverse("product-delete", kwargs={"pk": product.pk})
    response = client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
