from expenseList import ExpenseList
from expense import Expense
from decimal import Decimal, InvalidOperation

class Ui:
    def __init__(self, expense_list: ExpenseList):
        self.expense_list = expense_list

    def menu(self):
        print("1. Add expense")
        print("2. Edit expense")
        print("3. Delete expense")
        print("4. View expenses")
        print("5. View expenses by category")
        print("6. View total spent")
        print("7. Quit")
        print("Please type a number 1 to 7 to continue")

    def start(self):
        while(True):
            self.menu()
            response = input("Input: ").strip()

            if response == "1":
                self.add()

            elif response == "2":
                self.edit()

            elif response == "3":
                self.delete()

            elif response == "4":
                self.view()

            elif response == "5":
                self.show_by_category()

            elif response == "6":
                self.show_total()

            elif response == "7":
                break


    def edit(self):
        print()
        print("Please enter the ID of the expense to be edited")
        given_id = input("Input: ")

        try:
            given_id = int(given_id)
        except ValueError:
            print("Error: please enter a valid ID")
            return

        if self.expense_list.delete_expense(given_id):
            self.add()
        else:
            print("No expense with that ID found")


    def add(self):
        print()
        print("Please type the expense in the format 'description/cost/category")
        response = input("Input: ")
        splitResponse = response.split("/")

        if len(splitResponse) != 3:
            print("Error: please enter the expense in the format 'description/cost/category")
            print() 
            return
        
        description = splitResponse[0]

        try:
            cost = Decimal(splitResponse[1])
        except InvalidOperation:
            print("Please enter a valid cost")
            print()
            return
        
        category = splitResponse[2]

        expense_id = self.expense_list.create_id()

        self.expense_list.add_expense(Expense(description, cost, category, expense_id))
        print(f"Expense added with ID {expense_id}")
        print()


    def delete(self):
        print()
        print("Please enter the ID of the expense to be deleted")
        given_id = input("Input: ")

        try:
            given_id = int(given_id)
        except ValueError:
            print("Error: please enter a valid ID")
            return

        if self.expense_list.delete_expense(given_id):
            print(f"Expense with ID {given_id} successfully deleted")
            print()
        else:
            print("No expense with that ID found")
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

