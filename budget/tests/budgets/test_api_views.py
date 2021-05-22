import pytest
from unittest.mock import ANY

from django.urls import reverse
from model_bakery import baker
from rest_framework import status


@pytest.mark.parametrize(
    'method, view_name, view_kwargs', (
        ('get', 'budgets:expense-list', None),
        ('get', 'budgets:income-list', None),
        ('get', 'budgets:category-list', None),
        ('get', 'budgets:budget-list', None),
    )
)
@pytest.mark.parametrize('logged', (True, False))
@pytest.mark.django_db
def test_list_view_permissions(
    api_client, method, view_name,
    view_kwargs, user_fixture, logged
):
    if logged:
        api_client.force_login(user_fixture)
    method = getattr(api_client, method)
    response = method(reverse(view_name, kwargs=view_kwargs))
    expected_status = status.HTTP_200_OK if logged else status.HTTP_401_UNAUTHORIZED

    assert response.status_code == expected_status


@pytest.mark.django_db
def test_budget_list_view(user_fixture, api_client):
    user = baker.make('core.User')
    baker.make(
        'core.Budget',
        name=baker.seq('test Budget'),
        owner=user_fixture,
        _quantity=3
    )
    baker.make(
        'core.Budget',
        name='test Budget4',
        owner=user
    )
    api_client.force_login(user_fixture)
    response = api_client.get(reverse('budgets:budget-list'))

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [
        {
            'owner': ANY,
            'name': 'test Budget1',
            'incomes': [],
            'expenses': []
        }, {
            'owner': ANY,
            'name': 'test Budget2',
            'incomes': [],
            'expenses': []
        }, {
            'owner': ANY,
            'name': 'test Budget3',
            'incomes': [],
            'expenses': []
        },
    ]


@pytest.mark.django_db
def test_income_list_view(user_fixture, api_client, category_fixture, budget_fixture):
    baker.make(
        'core.Income',
        value=baker.seq(1234.5),
        category=category_fixture,
        budget=budget_fixture,
        _quantity=2
    )

    api_client.force_login(user_fixture)
    response = api_client.get(reverse('budgets:income-list'))

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [
        {
            'value': 1235.5,
            'category': ANY
        }, {
            'value': 1236.5,
            'category': ANY
        }
    ]


@pytest.mark.django_db
def test_expense_list_view(user_fixture, api_client, category_fixture, budget_fixture):
    baker.make(
        'core.Expense',
        value=baker.seq(1234.5),
        category=category_fixture,
        budget=budget_fixture,
        _quantity=2
    )

    api_client.force_login(user_fixture)
    response = api_client.get(reverse('budgets:expense-list'))

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [
        {
            'value': 1235.5,
            'category': ANY
        }, {
            'value': 1236.5,
            'category': ANY
        }
    ]


@pytest.mark.django_db
def test_category_list_view(user_fixture, api_client):
    baker.make(
        'core.Category',
        name=baker.seq('category'),
        description=baker.seq('test description '),
        _quantity=3
    )

    api_client.force_login(user_fixture)
    response = api_client.get(reverse('budgets:category-list'))

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [
        {
            'name': 'category1',
            'description': 'test description 1'
        }, {
            'name': 'category2',
            'description': 'test description 2'
        }, {
            'name': 'category3',
            'description': 'test description 3'
        },
    ]


@pytest.mark.django_db
def test_category_create_success(user_fixture, api_client):
    data = {
        'name': 'job',
        'description': 'money from work'
    }
    api_client.force_login(user_fixture)

    response = api_client.post(reverse('budgets:category-list'), data)

    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == data
