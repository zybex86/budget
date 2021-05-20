from django.urls import path, include
from rest_framework.routers import DefaultRouter

from budgets.views import BudgetViewSet


router = DefaultRouter()
router.register(r'budgets', BudgetViewSet)

app_name = 'budgets'

urlpatterns = [
    path('', include(router.urls))
]
