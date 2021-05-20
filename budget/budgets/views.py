from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin

from budgets.serializers import BudgetSerializer
from core.models import Budget


class BudgetViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = Budget.objects.all()
    serialzer_class = BudgetSerializer

    def get_queryset(self):
        return Budget.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
