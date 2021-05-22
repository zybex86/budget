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

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == [
            {
                'owner': 1,
                'name': 'test Budget1',
                'incomes': [],
                'expenses': []
            }, {
                'owner': 1,
                'name': 'test Budget2',
                'incomes': [],
                'expenses': []
            }, {
                'owner': 1,
                'name': 'test Budget3',
                'incomes': [],
                'expenses': []
            },
        ]
