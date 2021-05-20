import pytest

from django.urls import reverse
from model_bakery import baker
from rest_framework import status


@pytest.mark.django_db
class TestBudgetsViews:

    def test_budget_list_view(self, user_fixture, api_client):
        baker.make(
            'core.Budget',
            name=baker.seq('test Budget'),
            owner=user_fixture,
            _quantity=3
        )
        api_client.force_login(user_fixture)
        response = api_client.get(reverse('budgets:budget-list'))

        assert response.status == status.HTTP_200_OK
        assert response.json() == {

        }
