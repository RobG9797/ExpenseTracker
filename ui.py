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
            print()
            return

        expense = self.expense_list.get_expense_by_id(given_id)
        if expense is None:
            print("Error: no expense with that ID")
            print()
            return 

        details = self.get_expense_details()

        if details is None:
            return
        
        self.expense_list.edit_expense(given_id, details[0], details[1], details[2])

        print("Expense edited")
        print()


    def get_expense_details(self):
        print("Please type the expense in the format 'description/cost/category")
        response = input("Input: ")
        splitResponse = response.split("/")

        if len(splitResponse) != 3:
            print("Error: please enter the expense in the format 'description/cost/category")
            print() 
            return None
        
        description = splitResponse[0].strip()
        if description == "":
            print("Description cannot be empty")
            return None

        try:
            cost = Decimal(splitResponse[1])
        except InvalidOperation:
            print("Please enter a valid cost")
            return None

        if cost < 0:
            print("Please enter a valid cost")
            print()
            return None
        
        category = splitResponse[2].strip()
        if category == "":
            print("Category cannot be empty")
            return None

        return (description, cost, category)


    def add(self):
        print()
        details = self.get_expense_details()
        
        if details is None:
            return None
        (description, cost, category) = details

        expense_id = self.expense_list.add_expense(Expense(description, cost, category))
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
            return None

        if self.expense_list.delete_expense(given_id):
            print(f"Expense with ID {given_id} successfully deleted")
            print()
        else:
            print("No expense with that ID found")
            print()
            return None
        
    def view(self):
        print()
        print("All expenses:")
        for expense in self.expense_list.get_all_expenses():
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
        returned_values = self.expense_list.select_by_category(category)
        if not returned_values:
            print("No expenses in this category ")
            print()
            return
        
        print(f"Expenses in {category} category")
        for expense in returned_values:
            print(expense)

        print()
        print(f"Total spent in {category} category: £{self.expense_list.sum_by_category(category)}")
        print()

