from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):

    def create_user(self, username, password=None, **kwargs):
        """Create and save a new user"""
        if not username:
            raise ValueError('Users must have a username address!')
        user = self.model(username=username, **kwargs)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, password):
        """Create a superuser"""
        user = self.create_user(username, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model supporting email instead of username"""
    username = models.CharField(max_length=64, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'


class Category(models.Model):
    name = models.CharField(_('category'), max_length=255)
    description = models.CharField(_('description'), max_length=255, null=True)

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')
        ordering = ('name',)


class Budget(models.Model):
    name = models.CharField(_('name'), max_length=255)
    owner = models.ForeignKey(
        User,
        related_name='owners',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _('budget')
        verbose_name_plural = _('budgets')
        ordering = ('name',)


class BaseIncomeExpenseModel(models.Model):
    name = models.CharField(_('name'), max_length=255)

    class Meta:
        abstract = True


class Income(BaseIncomeExpenseModel):
    income = models.FloatField(_('income'))
    category = models.ForeignKey(
        Category,
        related_name='incomes',
        on_delete=models.CASCADE
    )
    budget = models.ForeignKey(
        Budget,
        related_name='incomes',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.income)

    class Meta:
        verbose_name = _('income')
        verbose_name_plural = _('incomes')
        ordering = ('pk',)


class Expense(BaseIncomeExpenseModel):
    expense = models.FloatField(_('expense'))
    category = models.ForeignKey(
        Category,
        related_name='expenses',
        on_delete=models.CASCADE
    )
    budget = models.ForeignKey(
        Budget,
        related_name='expenses',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.expense)

    class Meta:
        verbose_name = _('expense')
        verbose_name_plural = _('expenses')
        ordering = ('pk',)
