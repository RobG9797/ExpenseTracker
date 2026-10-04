from expenseList import ExpenseList
from expense import Expense
from decimal import Decimal

class Ui:
    def __init__(self, expenseList: ExpenseList):
        self.expenseList = expenseList

    def start(self):
        while(True):
            self.menu()
            response = input("Input: ").strip()

            if response == "1":
                self.add()

            elif response == "2":
                self.view()

            elif response == "3":
                self.show_total()

            elif response == "4":
                self.show_by_category()

            elif response == "5":
                break

    def add(self):
        print("Please type the expense in the format 'description/cost/category")
        response = input("Input: ")
        splitResponse = response.split("/")
        description = splitResponse[0]
        cost = Decimal(splitResponse[1])
        category = splitResponse[2]
        self.expenseList.add_expense(Expense(description, cost, category))
        print()

    def view(self):
        self.expenseList.view_expenses()
        print()

    def show_total(self):
        self.expenseList.total_spent()
        print()

    def show_by_category(self):
        response = input("Please enter the name of the category: ")
        print()
        self.expenseList.view_expense_category(response)
        print()

    def menu(self):
        print("1. Add expense")
        print("2. View expenses")
        print("3. Show total spent")
        print("4. View expenses by category")
        print("5. Quit")
        print("Please type a number 1 to 4 to continue")

