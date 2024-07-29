#!/usr/bin/python3

"""2. C is fun! - Flask web framework"""

from flask import Flask
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


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
