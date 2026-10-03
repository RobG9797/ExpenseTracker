from expense import Expense

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
        for expense in self.expenses:
            if expense.get_category() == category.lower():
                print(f"{expense.get_description().title()} / £{expense.get_cost()}")
