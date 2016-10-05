from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.ext.mysql import MySQL

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:root@localhost:3306/expenses_management_system"
db = SQLAlchemy(app)
db.create_all()

class Expenses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    email = db.Column(db.String(20))
    category = db.Column(db.String(20))
    description = db.Column(db.String(30))
    link = db.Column(db.String(20))
    estimated_costs = db.Column(db.Integer)
    submit_date = db.Column(db.Date, server_default=db.func.current_Date(), nullable=False)
    status = db.Column(db.String(20))
    decision_date = db.Column(db.Date)
        
    def __init__(self, name, email, category, description, link, estimated_costs):
        self.name = name;
        self.email = email
        self.category = category
        self.description = description
        self.link = link
        self.estimated_costs = estimated_costs
       
        