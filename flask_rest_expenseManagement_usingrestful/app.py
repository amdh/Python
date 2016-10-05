from flask import Flask
from flask_restful import Resource, Api
from resources.user import User
from resources.ExpenseManagement import ExpenseManagement
from models.Expenses import Expenses


app = Flask(__name__)
api = Api(app)


api.add_resource(User,'/User')
api.add_resource(ExpenseManagement, '/v1/expenseManagement')

if __name__ == '__main__':
    app.run(debug=True)
