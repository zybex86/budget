import pytest

from django.contrib.auth import get_user_model

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
