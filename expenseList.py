from expense import Expense
from decimal import Decimal

class ExpenseList:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense:Expense):
        self.expenses.append(expense)

    def view_expenses(self):
        print("All expenses:")
        for expense in self.expenses:
            print(expense)

    def view_expense_category(self, category:str):
        category_total = Decimal("0.0")
        print(f"Purchases in {category} category:")
        for expense in self.expenses:
            if expense.get_category() == category.lower().strip():
                category_total += expense.get_cost()
                print(f"{expense.get_description().title()} / £{expense.get_cost()}")
        print(f"Total spent in {category} category: £{category_total}")

    def total_spent(self):
        total = Decimal("0.0")
        for expense in self.expenses:
            total += expense.get_cost()
        print(f'Total spent: £{total}')
