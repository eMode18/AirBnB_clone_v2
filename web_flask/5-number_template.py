#!/usr/bin/python3
"""
This code initializes a Flask web application and defines various routes.
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_route():
    """
    Route to display 'Hello HBNB!' when accessed.
    Returns:
        str: "Hello HBNB"
    """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """
    Route to display 'HBNB' when accessed.
    Returns:
        str: "HBNB"
    """
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    Route to display “C ” followed by the provided text,
    replacing underscores with spaces.
    Returns:
        str: "C <text>"
    """
    return "C {}".format(text.replace('_', ' '))

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text="is_cool"):
    """
    Route to display “Python ” followed by the given text,
    replacing underscores with spaces.
    Defaults to "is cool" if no text provided.
    Returns:
        str: "Python <text>"
    """
    return "Python {}".format(text.replace('_', ' '))

@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """
    Route to display “n is a number” only if n is an integer.
    Returns:
        str: "{} is a number".format(n)
    """
    return "{} is a number".format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template_route(n):
    """
    Route to display an HTML template if n is an integer:
    - Displays "Number: n" inside an H1 tag in the template.
    Returns:
        html: Template displaying the value of n
    """
    return render_template('5-number.html', n=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

