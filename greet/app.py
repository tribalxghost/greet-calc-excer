from flask import Flask


app = Flask(__name__)


@app.route('/welcome')
def welcome():
    return "Welcome"

@app.route('/welcome/<welcome>')
def welcomeMessage(welcome):
    return f"welcome {welcome}"
