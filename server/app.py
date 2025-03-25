#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"


@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return f'{parameter}'

@app.route('/count/<int:number>')
def count(number):
    # if number < 1:
    #     return "Enter an integer greater than 0", 400
    # return "\n".join(str(i) for i in range(number))
    numbers = f""
    for i in range(number):
        numbers += f"{i}\n"
    return numbers

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '%':
        # if num2 == 0:
        #     return 'division by 0 not accepted', 400
        result = num1 % num2
    elif operation == 'div':
        # if num2 == 0:
        #     return 'division by 0 not accepted', 400
        result = num1 / num2
    else:
        return "unsupported operation"
    
    return f"{result}"
    
    
    

    

if __name__ == '__main__':
    app.run(port=5555, debug=True)
