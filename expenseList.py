from expense import Expense
from decimal import Decimal
import sqlite3

class ExpenseList:

    def get_all_expenses(self):
        connection = sqlite3.connect("expenses.db")
        cursor = connection.cursor()

        cursor.execute("""
            SELECT description, cost_pence, category, id
            FROM expenses
        """) 

        rows = cursor.fetchall() # rows is a list that holds each row as a tuple 
        connection.close()

        # For each tuple in the list, create a new Expense object and append to the expenses list
        expenses = []
        for expense in rows:  
            expenses.append(  
                Expense(
                    expense[0], 
                    Decimal(expense[1]) / 100, # converts cost from pence to decimal
                    expense[2], 
                    expense[3]
                    )
                )
        return expenses
    
    # Inserts the selected Expense object into the expenses table
    def add_expense(self, expense:Expense):         
        connection = sqlite3.connect("expenses.db") 
        cursor = connection.cursor()
        cost_pence = int(expense.get_cost() * 100)  

        cursor.execute(
            """
            INSERT INTO expenses (description, cost_pence, category)
            VALUES (?, ?, ?)
            """,
            (
                expense.get_description(),
                cost_pence,
                expense.get_category()
            )
        )
        expense_id = cursor.lastrowid
        connection.commit()
        connection.close()
        return expense_id

    def get_expense_by_id(self, expense_id):
        connection = sqlite3.connect("expenses.db")
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT * FROM expenses
            WHERE id = ?
            """,
            (expense_id,)
        )

        selected = cursor.fetchone()
        connection.close()

        return Expense(selected[0], selected[1], selected[2], selected[3])

    def delete_expense(self, expense_id:int):
        connection = sqlite3.connect("expenses.db")
        cursor = connection.cursor()

        cursor.execute(
            """
            DELETE FROM expenses
            WHERE id = ?
            """, 
            (expense_id,)
        )
        
        # returns True if a row was deleted
        deleted = cursor.rowcount > 0  
        connection.commit()
        connection.close()
        return deleted
 
    def total_by_category(self, category):
        category_total = Decimal("0.0")
        for expense in self.get_all_expenses():
            if expense.get_category() == category.lower().strip():
                category_total += expense.get_cost()
        return category_total

    def expenses_by_category(self, category):
        category = category.lower().strip()
        returned_expenses = []
        for expense in self.get_all_expenses():
            if expense.get_category() == category:
                returned_expenses.append(expense)
        return returned_expenses

    def total_spent(self):
        total = Decimal("0.0")
        for expense in self.get_all_expenses():
            total += expense.get_cost()
        return total
