#!/usr/bin/python3
"""
This script initializes a Flask web application and defines various routes.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_route():
    """
    Route: '/'
    Function: hello_route
    Behavior: Displays 'Hello HBNB!' when accessed.
    Returns:
        str: "Hello HBNB"
    """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """
    Route: '/hbnb'
    Function: hbnb_route
    Behavior: Displays 'HBNB' when accessed.
    Returns:
        str: "HBNB"
    """
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    Route: '/c/<text>'
    Function: c_route
    Behavior: Displays “C ” followed by the value of the text variable
              (replace underscore '_' symbols with a space ' ')
    Params:
        text (str): The text provided in the URL
    Returns:
        str: "C <text>"
    """
    return f"C {text.replace('_', ' ')}"

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text="is_cool"):
    """
    Routes: '/python' and '/python/<text>'
    Function: python_route
    Behavior: Displays “Python ” followed by the value of the text variable
              (replace underscore _ symbols with a space )
    Params:
        text (str): The text provided in the URL. Default: "is_cool"
    Returns:
        str: "Python <text>"
    """
    return f"Python {text.replace('_', ' ')}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

