from flask import Flask, jsonify, abort, request
from flask.ext.restless import APIManager
from flask.ext.sqlalchemy import SQLAlchemy



app = Flask(__name__)


if __name__ == '__main__':
    app.run(debug=True)
