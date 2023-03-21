# Put your app in here.

from flask import Flask
from flask import request
from operations import add, sub, mult, div

app = Flask(__name__)


@app.route('/add')
def addN():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"Adds {a} and {b} result = {add(a, b)}"

@app.route('/sub')
def subN():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"Subtracts {a} and {b} result = {sub(a, b)}"

@app.route('/mult')
def multN():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"Adds {a} and {b} result = {mult(a, b)}"

@app.route('/div')
def divN():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"Adds {a} and {b} result = {int(div(a, b))}"



@app.route('/math/<func>')
def mathN(func):
    a = int(request.args["a"])
    b = int(request.args["b"])
    ops = {
    "add":add(a, b),
    "sub":sub(a, b),
    "div":div(a, b),
    "mult":mult(a, b)
    }

    return f"This {int(ops[func])}"
    # return f"Equals {ops[func](a, b)}"


