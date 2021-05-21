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
    income = IncomeSerializer(many=True)
    expense = ExpenseSerializer(many=True)

    class Meta:
        model = Budget
        fields = ('owner', 'name', 'income', 'expense',)
