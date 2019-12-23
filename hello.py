from werkzeug.wrappers import Request, Response
from flask import Flask
app = Flask(__name__)


@app.route('/<int:num1>,<int:num2>')
def sum_of_numbers(num1,num2):
    sum=num1+num2
    return '%d' % sum


if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 5000, app)
