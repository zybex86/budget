from django.urls import path, include
from rest_framework.routers import DefaultRouter

from budgets.views import BudgetViewSet, CategoryViewSet, ExpenseViewSet, IncomeViewSet


router = DefaultRouter()
router.register(r'budgets', BudgetViewSet)
router.register(r'incomes', IncomeViewSet)
router.register(r'expenses', ExpenseViewSet)
router.register(r'categories', CategoryViewSet)

app_name = 'budgets'

urlpatterns = [
    path('', include(router.urls))
]
