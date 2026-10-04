from expenseList import ExpenseList
from expense import Expense
from decimal import Decimal

class Ui:
    def __init__(self, expense_list: ExpenseList):
        self.expense_list = expense_list

    def menu(self):
        print("1. Add expense")
        print("2. View expenses")
        print("3. View expenses by category")
        print("4. View total spent")
        print("5. Quit")
        print("Please type a number 1 to 5 to continue")

    def start(self):
        while(True):
            self.menu()
            response = input("Input: ").strip()

            if response == "1":
                self.add()

            elif response == "2":
                self.view()

            elif response == "3":
                self.show_by_category()

            elif response == "4":
                self.show_total()

            elif response == "5":
                break

    def add(self):
        print()
        print("Please type the expense in the format 'description/cost/category")
        response = input("Input: ")
        splitResponse = response.split("/")
        description = splitResponse[0]
        cost = Decimal(splitResponse[1])
        category = splitResponse[2]
        self.expense_list.add_expense(Expense(description, cost, category))
        print("Expense added!")
        print()

    def view(self):
        print()
        print("All expenses:")
        for expense in self.expense_list.expenses:
            print(expense)
        print()

    def show_total(self):
        print()
        print(f"Total spent: £{self.expense_list.total_spent()}")
        print()

    def show_by_category(self):
        print()
        category = input("Please enter the name of the category: ").strip().lower()
        print()
        print(f"Expenses in {category} category")
        for expense in self.expense_list.expenses_by_category(category):
            print(expense)
        print()
        print(f"Total spent in {category} category: £{self.expense_list.total_by_category(category)}")
        print()

