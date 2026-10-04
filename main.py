from expenseList import ExpenseList
from expense import Expense
from decimal import Decimal

expenselist = ExpenseList()

expenselist.add_expense(Expense("bought flowers", Decimal("1.25"), "recreation"))
expenselist.add_expense(Expense("bought guitar", Decimal("1.25"), "recreation"))
expenselist.add_expense(Expense("bought food", Decimal("1.25"), "food"))

expenselist.view_expense_category("recreation")
expenselist.total_spent()