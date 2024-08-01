#!/usr/bin/python3

"""2. C is fun! - Flask web framework"""

from flask import Flask, render_template
from flask import request

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """A route function"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """A route function that displays HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    """
    C is fun
    Route function to display c followed by a text from the query
    """
    remove_underscore = text.replace("_", " ")

    return "C " + remove_underscore


@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """Python is cool function - route /python"""
    remove_underscore = text.replace("_", " ")
    return "Python " + remove_underscore


@app.route("/number/<int:n>", strict_slashes=False)
def is_a_number(n):
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def template_number(n):
    return render_template('5-number.html', number=n)

if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
