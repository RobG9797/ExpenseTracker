from decimal import Decimal

class Expense:
    def __init__(self, description:str, cost:Decimal, category:str, expense_id:int):
        self.description = description
        self.cost = cost
        self.category = category.lower().strip()
        self.expense_id = expense_id

    def set_description(self, description:str):
        self.description = description

    def set_cost(self, cost:Decimal):
        self.cost = self.cost

    def set_category(self, category:str):
        self.category = category

    def get_cost(self):
        return self.cost

    def get_id(self):
        return self.expense_id


    def get_description(self):
        return self.description


    def get_category(self):
        return self.category


    def __str__(self):
        return f"{self.expense_id}. {self.description} / £{self.cost} / {self.category}"