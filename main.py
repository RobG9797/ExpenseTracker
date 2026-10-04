from expenseList import ExpenseList
from expense import Expense
from decimal import Decimal
from ui import Ui

expense_list = ExpenseList()
ui = Ui(expense_list)
ui.start()


