from expense import Expense
from decimal import Decimal
from pathlib import Path
import json

class ExpenseList:
    def __init__(self):
        self.expenses = self.load_expenses()

    def load_expenses(self):
        file_path = Path("expenses.json")

        if file_path.exists():
            with open(file_path, "r") as file:
                data = json.load(file)
                expenses = []
                for expense_dict in data:
                    description = expense_dict["description"]
                    cost = Decimal(expense_dict["cost"])
                    category = expense_dict["category"]
                    expense_id = int(expense_dict["id"])
                    expenses.append(Expense(description, cost, category, expense_id))
                return expenses
        else:
            return []

    def add_expense(self, expense:Expense):
        self.expenses.append(expense)
        self.save_expenses()

    def save_expenses(self):
        data = []
        for expense in self.expenses:
            expense_as_dict = {
                "description": expense.get_description(),
                "cost": str(expense.get_cost()),
                "category": expense.get_category(),
                "id": expense.get_id()
            }
            data.append(expense_as_dict)

        with open("expenses.json", "w") as file:
            json.dump(data, file, indent=4)


    def create_id(self):
        lowest_id = 1

        with open("expenses.json", "r") as file:
            data = json.load(file)
            for expense in data:
                if lowest_id == expense["id"]:
                    lowest_id += 1

        return lowest_id
                


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
