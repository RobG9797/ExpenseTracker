from expenseList import ExpenseList
from expense import Expense

expenselist = ExpenseList()

expenselist.add_expense(Expense("bought flowers", 1.25, "recreation"))

expenselist.view_expense_category("recreation")