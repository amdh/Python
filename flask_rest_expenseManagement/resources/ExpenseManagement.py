from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.mysql import MySQL

app = Flask(__name__)


db = SQLAlchemy(app)

class ExpenseManagement(Resource):
    
    def get(self):
        expenses = Expenses.query.all()
        return { 'name' : 'amruta', 'status':'pending'}

    def post(self):
        return {'status':'approved'}

    @app.route("/<int:id>")
    def put(self):
        return { 'status' : 'updated' , 'name' : 'amz'}

    @app.route("/<int:id>")
    def delete(self):
        return { 'status' : 'deleted'}