class Budget:
    def __init__(self, budget_name, budget_amount):
        self._budget_name = budget_name
        self._budget_amount = budget_amount

    @property
    def name(self):
        return self._budget_name

    @property
    def amount(self):
        return self._budget_amount

    @name.setter
    def name(self, budget_name):
        self._budget_name = budget_name

    @amount.setter
    def amount(self, budget_amount):
        self._budget_amount = budget_amount


class Expenses:
    def __init__(self, expense_name, expense_amount):
        self._expense_name = expense_name
        self._expense_amount = expense_amount

    @property
    def name(self):
        return self._expense_name

    @property
    def amount(self):
        return self._expense_amount

    @name.setter
    def name(self, expense_name):
        self._expense_name = expense_name

    @amount.setter
    def amount(self, expense_amount):
        self._expense_amount = expense_amount


test = Expenses("", 0)
test.name = "Alex"
print(test.name)
