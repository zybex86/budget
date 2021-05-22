from rest_framework import serializers

from core.models import Budget, Category, Expense, Income


class ExpenseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expense
        fields = ('category', 'value',)


class IncomeSerializer(serializers.ModelSerializer):

    class Meta(ExpenseSerializer.Meta):
        model = Income


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name', 'description')


class BudgetSerializer(serializers.ModelSerializer):
    incomes = IncomeSerializer(many=True)
    expenses = ExpenseSerializer(many=True)

    class Meta:
        model = Budget
        fields = ('owner', 'name', 'incomes', 'expenses',)
