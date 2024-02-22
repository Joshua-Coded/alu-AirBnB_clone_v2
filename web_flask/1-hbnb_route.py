#!/usr/bin/python3
""" Script for adding more functions"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ function that displays " hello hbnb" """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ function that displays "hbnb" """
    return 'HBNB'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)