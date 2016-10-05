from flask import Flask, jsonify, abort

app = Flask(__name__)

expenses = [
    {
    "id" : "123456",
    "name" : "Foo Bar",
    "email" : "foo@bar.com",
    "category" : "office supplies|travel|training",
    "description" : "iPad for office use",
    "link" : "http://www.apple.com/shop/buy-ipad/ipad-pro",
    "estimated_costs" : "700",
    "submit_date" : "09-08-2016",
    "status" : "pending|approved|rejected|overbudget",
    "decision_date" : "09-10-2016"
}
]

@app.route("/v1/expenses", methods=['GET'])
def getExpenses():
    return jsonify({'expenses':expenses})


@app.route('/v1/expenses', methods=['POST'])
def createExpense():
    if not request.json or not 'id' in request.json:
        abort(400)
    expense = {
        'id': expenses[-1]['id'] + 1,
        'name': request.json['name'],
        'description': request.json.get('description', ""),
        'estimated_cost': request.json.get['cost']
    }
    expenses.append(expense)
    return jsonify({'expense': expense}), 201

@app.route('/v1/expenses/<int:id>', methods=['PUT'])
def updateExpense(id):
    expense = [expense for expense in expenses if expense['id'] == id]
    if len(expense) == 0:
        abort(404)
    if not request.json:
        abort(400)
   
    expense[0]['name'] = request.json.get('name', expense[0]['name'])
   
    return jsonify({'expense': expense[0]})

@app.route('/v1/expenses/<int:id>', methods=['DELETE'])
def deleteExpense(id):
    expense = [expense for expense in expenses if expense['id'] == id]
    if len(expense) == 0:
        abort(404)
    expenses.remove(expense[0])
    return jsonify({'result': True})

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')