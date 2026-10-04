from expense import Expense
from decimal import Decimal

class ExpenseList:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense:Expense):
        self.expenses.append(expense)

    def total_by_category(self, category):
        category_total = Decimal("0.0")
        for expense in self.expenses:
            if expense.get_category() == category.lower().strip():
                category_total += expense.get_cost()
        return category_total

    def expenses_by_category(self, category):
        category = category.lower().strip()
        returned_expenses = []
        for expense in self.expenses:
            if expense.get_category() == category:
                returned_expenses.append(expense)
        return returned_expenses

    def total_spent(self):
        total = Decimal("0.0")
        for expense in self.expenses:
            total += expense.get_cost()
        return total
