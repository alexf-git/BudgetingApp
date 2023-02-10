class Budget:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
        self.expenses = []

    def __str__(self):
        return f"{self.name} = {self.amount} / {self.expenses}"

    def add_expense(self, expense):
        self.expenses.append(expense)

    def get_remaining_budget(self):
        for items in self.expenses:
            self.amount -= items.amount
        return self.amount


class Expense:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def __str__(self):
        return f"{self.name} = {self.amount}"


# Testing class functionality

# budget_name = "January Budget"
# budget_amount = 1000
#
# b_obj = Budget(budget_name, budget_amount)
# print(b_obj)
# bills = Expense("Rent", 500)
# b_obj.add_expense(bills)
# print(b_obj)
#
# b_obj.get_remaining_budget()
# print(b_obj)
