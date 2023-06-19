#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = "\n".join(str(num) for num in range(parameter))
    return numbers

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    result = None

    if operation == '+':
        result = int(num1) + int(num2)
    elif operation == '-':
        result = int(num1) - int(num2)
    elif operation == '*':
        result = int(num1) * int(num2)
    elif operation == 'div':
        result = int(num1) / int(num2)
    elif operation == '%':
        result = int(num1) % int(num2)

    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
