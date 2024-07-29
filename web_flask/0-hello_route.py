#!/usr/bin/python3

"""0. Hello Flask - Flask web framework"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	"""A route function"""
	return "Hello HBNB!"


if __name__ == "__main__":
	app.run(port=5000, host= "0.0.0.0")
