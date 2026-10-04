from expenseList import ExpenseList
from expense import Expense
from decimal import Decimal
from ui import Ui

expenselist = ExpenseList()
ui = Ui(expenselist)
ui.start()


