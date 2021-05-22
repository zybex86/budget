import pytest

from django.contrib.auth import get_user_model
from django.urls import reverse
from model_bakery import baker
from rest_framework import status

CREATE_USER_URL = 'user:create'
USER_CREATE_DATA = {
    'username': 'new_test_user',
    'password': '$Tr0ngP4ss',
    'name': 'Teapot'
}


@pytest.mark.django_db
def test_create_valid_user_success(api_client):
    response = api_client.post(reverse(CREATE_USER_URL), USER_CREATE_DATA)

    assert response.status_code == status.HTTP_201_CREATED
    user = get_user_model().objects.get(**response.data)

    assert user.check_password(USER_CREATE_DATA['password'])
    assert 'password' not in response.data


@pytest.mark.django_db
def test_user_already_exists(api_client):
    baker.make('core.User', **USER_CREATE_DATA)

    response = api_client.post(reverse(CREATE_USER_URL), USER_CREATE_DATA)

    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_password_too_short(api_client):
    data = USER_CREATE_DATA
    data['password'] = 'pw'

    response = api_client.post(reverse(CREATE_USER_URL), USER_CREATE_DATA)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert not get_user_model().objects.filter(**USER_CREATE_DATA).exists()
