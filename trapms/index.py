from flask import Flask
from flask import jsonify
from flask_pymongo import PyMongo


app = Flask(__name__)


@app.route("/")
def hello():
    say = {'greeting': 'Hello, World!'}
    return jsonify(say)
