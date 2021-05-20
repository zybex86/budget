from rest_framework import serializers

from core.models import Budget, Income, Expense


class ExpenseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expense
        fields = ('category', 'expense',)


class IncomeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Income
        fields = ('category', 'income',)


class BudgetSerializer(serializers.ModelSerializer):
    incomes = IncomeSerializer(many=True)
    expenses = ExpenseSerializer(many=True)

    class Meta:
        model = Budget
        fields = ('owner', 'name', 'incomes', 'expenses',)
