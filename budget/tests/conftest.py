import pytest

from django.contrib.auth import get_user_model
from model_bakery import baker
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user_fixture():
    user = get_user_model().objects.create_user(
        'test',
        'testPass'
    )

    return user


@pytest.fixture
def admin_fixture():
    user = get_user_model().objects.create_superuser(
        'admin',
        'testPass'
    )

    return user


@pytest.fixture
def category_fixture():
    return baker.make(
        'core.Category',
        name='test Category',
    )


@pytest.fixture
def budget_fixture(user_fixture):
    return baker.make(
        'core.Budget',
        name='test Budget',
        owner=user_fixture
    )
