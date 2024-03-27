import pytest
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from apps.accounts.models import CustomUser
from apps.establishment.models import Establishment

client = APIClient()



# Тесты для представления EstablishmentModelViewSet
@pytest.mark.django_db
def test_create_establishment():

    user = CustomUser.objects.create(
        email="test@example.com", 
        role="manager", 
        password="password"
        )
    client.force_authenticate(user=user)
    
    establishment_data = {
        "name": "Test Establishment",
        "description": "Test Description",
        "locations": "Test Location",
        "opening_hours": "Test Hours",
        "requirements": "Test Requirements",
        "manager": user.id 
    }
    response = client.post('/api/v1/establishment/create/', establishment_data)
    assert response.status_code == status.HTTP_201_CREATED
    assert Establishment.objects.filter(name="Test Establishment").exists()


@pytest.mark.django_db
def test_update_establishment():
    user = CustomUser.objects.create(email="test@example.com", role="manager", password="password")
    client.force_authenticate(user=user)
    
    establishment = Establishment.objects.create(
        name="Test Establishment",
        description="Test Description",
        locations="Test Location",
        opening_hours="Test Hours",
        requirements="Test Requirements",
        manager=user 
    )
    new_establishment_data = {
        "name": "Updated Establishment",
        "description": "Updated Description",
    }
    response = client.put(f'/api/v1/establishment/update/{establishment.id}/', new_establishment_data)
    assert response.status_code == status.HTTP_200_OK
    updated_establishment = Establishment.objects.get(id=establishment.id)
    assert updated_establishment.name == "Updated Establishment"


@pytest.mark.django_db
def test_delete_establishment():
    user = CustomUser.objects.create(email="test@example.com", role="manager", password="password")
    client.force_authenticate(user=user)
    establishment = Establishment.objects.create(
        name="Test Establishment",
        description="Test Description",
        locations="Test Location",
        opening_hours="Test Hours",
        requirements="Test Requirements",
        manager=user
    )
    response = client.delete(f'/api/v1/establishment/delete/{establishment.id}/')
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not Establishment.objects.filter(id=establishment.id).exists()