#!/usr/bin/python3

"""1. HBNB - Flask web framework"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
	"""A route function"""
	return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
	"""A route function that displays HBNB"""
	return "HBNB"

if __name__ == "__main__":
	app.run(port=5000, host="0.0.0.0")
