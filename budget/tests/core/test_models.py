import pytest

from django.contrib.auth import get_user_model

from core.models import Budget, Category, Expense, Income


@pytest.mark.django_db
class TestUserModel:

    def test_create_user_success(self):
        """Test creating a new user"""
        username = 'test_user'
        password = "Testpass123$"
        user = get_user_model().objects.create_user(
            username=username,
            password=password
        )

        assert user.username == username
        assert user.check_password(password)

    def test_create_superuser_success(self):
        """Test creating a new user"""
        username = 'test_admin'
        password = "Testpass123$"
        user = get_user_model().objects.create_superuser(
            username=username,
            password=password
        )

        assert user.is_staff

    def test_new_user_invalid(self):
        """Test creating invalid user"""
        with pytest.raises(ValueError):
            get_user_model().objects.create_user(None, 'test123')


@pytest.mark.django_db
class TestOtherModels:

    def test_create_budget_success(self, user_fixture):
        """Test creating a new budget"""
        budget_name = 'Test budget'
        budget = Budget.objects.create(
            name=budget_name,
            owner=user_fixture
        )

        assert budget.name == budget_name
        assert budget.owner == user_fixture

    def test_create_category_success(self):
        name = 'test category'
        description = 'test category description'
        category = Category.objects.create(
            name=name,
            description=description
        )

        assert category.name == name
        assert category.description == description

    def test_create_income_success(self, category_fixture, budget_fixture):
        name = 'paycheck'
        ammount = 1234.5

        income = Income.objects.create(
            name=name,
            income=ammount,
            category=category_fixture,
            budget=budget_fixture
        )
        assert income.name == name
        assert income.income == ammount
        assert income.budget == budget_fixture
        assert income.category == category_fixture

    def test_create_expense_success(self, category_fixture, budget_fixture):
        name = 'credit'
        ammount = 1234.5

        expense = Expense.objects.create(
            name=name,
            expense=ammount,
            category=category_fixture,
            budget=budget_fixture
        )
        assert expense.name == name
        assert expense.expense == ammount
        assert expense.budget == budget_fixture
        assert expense.category == category_fixture
