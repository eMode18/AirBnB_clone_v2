#!/usr/bin/python3
"""
This code initializes a Flask web application.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_route():
    """
    Defines the route for the root URL ('/'), displaying 'Hello HBNB!'.
    
    Returns:
        str: The message "Hello HBNB"
    """
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

