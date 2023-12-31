#!/usr/bin/python3
"""
This code initializes a Flask web application and defines various routes.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_route():
    """
    Displays 'Hello HBNB!' when accessed.
    Returns:
        str: "Hello HBNB"
    """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """
    Displays 'HBNB' when accessed.
    Returns:
        str: "HBNB"
    """
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    Shows "C " followed by the provided text, replacing underscores with spaces.
    Returns:
        str: "C <text>"
    """
    return "C {}".format(text.replace('_', ' '))

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text="is_cool"):
    """
    Displays "Python " followed by the given text, replacing underscores with spaces.
    Defaults to "is cool" if no text provided.
    Returns:
        str: "Python <text>"
    """
    return "Python {}".format(text.replace('_', ' '))

@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """
    Shows "{n} is a number" if n is an integer.
    Returns:
        str: "{} is a number".format(n)
    """
    return "{} is a number".format(n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

