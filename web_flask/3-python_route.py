#!/usr/bin/python3
""" Script that runs a flask application"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ function that return " hello hbnb" """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ function that displays hbnb!"""
    return 'HBNB'



@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """ function that returns "C" followed by the value of the text"""
    return 'C {}'.format(text.replace('_', ''))


@app.route('/pythons', strict_slashes=False)
@app.route('/pythons/<text>', strict_slashes=False)
def python_is_cool(text = 'is  cool'):
    """ function that returns python followed by the value of the text"""
    return 'Python {}'.format(text.replace('_', ' '))



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)