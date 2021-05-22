from rest_framework import serializers

from core.models import Budget, Category, Expense, Income


class ExpenseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expense
        fields = ('category', 'expense',)


class IncomeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Income
        fields = ('category', 'income',)


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name', 'description')


class BudgetSerializer(serializers.ModelSerializer):
    incomes = IncomeSerializer(many=True, read_only=True)
    expenses = ExpenseSerializer(many=True, read_only=True)

    class Meta:
        model = Budget
        fields = ('owner', 'name', 'incomes', 'expenses',)
