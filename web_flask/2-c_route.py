#!/usr/bin/python3
"""
This code initializes a Flask web application with multiple routes.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """
    Defines the root route, displaying 'Hello HBNB!'.
    
    Returns:
        str: "Hello HBNB"
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """
    Defines the '/hbnb' route, displaying 'HBNB'.
    
    Returns:
        str: "The message HBNB"
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    Defines a dynamic route '/c/<text>', displaying "C " followed by the value of 'text'.
    Underscore '_' symbols in 'text' are replaced with spaces.
    
    Args:
        text (str): The text parameter from the URL

    Returns:
        str: "C <text>"
    """
    return "C {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

