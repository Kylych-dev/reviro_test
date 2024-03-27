import pytest
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

client = APIClient()



# ______________________________________________________________
# +++++++++++++++++++++++++
@pytest.mark.django_db
def test_register_user():
    payload = dict(
        email="user1@mail.ru",
        role="user",
        password="mirbekov 1993",
        password2="mirbekov 1993"
    )
    response = client.post('/api/v1/register/', payload)
    data = response.data
    assert data['email'] == payload['email']
    assert data['role'] == payload['role']
    assert 'password' not in data



@pytest.mark.django_db
def test_login_user():
    payload = dict(
        email="user1@mail.ru",
        role="user",
        password="mirbekov 1993",
        password2="mirbekov 1993"
    )
    client.post('/api/v1/register/', payload)

    response = client.post('/api/v1/login/', dict(email='user1@mail.ru', password='mirbekov 1993'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_login_user_fail():
    response = client.post('/api/v1/login/', dict(email='user1ail.ru', password='mirb1993'))
    assert response.status_code == 401



# ______________________________________________________________