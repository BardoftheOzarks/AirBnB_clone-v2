#!/usr/bin/python3
'''
Starts a Flask web application
'''
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def no_hello():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def sea(text):
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def cool_it(text='is_cool'):
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def numma(n):
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def my_first_template(n):
    return render_template('5-number.html', number=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
