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

    def select_by_category(self, category):
        connection = sqlite3.connect("expenses.db")
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT * FROM expenses
            WHERE category = ?
            """, (category,)
        )
        result = cursor.fetchall()
        connection.close()
        expenses = []
        for expense in result:
            expenses.append(Expense(expense[1], Decimal(expense[2]) / 100, expense[3], expense[0]))
        return expenses

    def sum_by_category(self, category):
        connection = sqlite3.connect("expenses.db")
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT SUM(cost_pence) 
            FROM expenses
            WHERE category = ?
            """, (category,)
        )
        result = cursor.fetchone()
        connection.close()
        return Decimal(result[0]) / 100 if result[0] is not None else Decimal("0.0")
        

    def edit_expense(self, expense_id, description, cost, category):
        connection = sqlite3.connect("expenses.db")
        cursor = connection.cursor()

        cost_pence = int(cost * 100)

        cursor.execute(
            """
            UPDATE expenses
            SET description = ? , cost_pence = ?, category = ?
            WHERE id = ?
            """, 
            (description, cost_pence, category, expense_id)
        )
        found = cursor.rowcount > 0

        connection.commit()
        connection.close()

        return found
    
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

        if selected is None:
            return None

        return Expense(selected[1], (Decimal(selected[2])) / 100, selected[3], selected[0])


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

    def total_spent(self):
        total = Decimal("0.0")
        for expense in self.get_all_expenses():
            total += expense.get_cost()
        return total
