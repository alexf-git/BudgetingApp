from flask import Flask, render_template, request
import budget

app = Flask(__name__)
e_list = []


@app.route('/', methods=['GET', 'POST'])
def main():
    name = request.form.get('budget_name')
    amount = request.form.get('budget_amount')

    b = budget.Budget(name, amount)

    return render_template('testing.html',
                           budget=b,
                           budget_name=b.name,
                           budget_amount=b.amount
                           )


@app.route('/expenses', methods=['GET', 'POST'])
def expenses():
    expense_name = request.form.get('expense_name')
    expense_amount = request.form.get('expense_amount')

    e = budget.Expenses(expense_name, expense_amount)

    e_list.append(e)

    return render_template('testing.html',
                           expense_name=e.name,
                           expense_amount=e.amount,
                           expense_list=e_list
                           )


if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug=True)
