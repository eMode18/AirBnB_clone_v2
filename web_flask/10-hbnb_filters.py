#!/usr/bin/python3
"""
Code to initialize a Flask web application:
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters_route():
    """
    Route to list all cities of states: Renders an HTML page displaying
    states, cities, and amenities sorted by name A->Z.
    Returns:
        html: Template listing states, cities, and amenities sorted
        alphabetically by name
    """
    data = {
        "states": storage.all("State").values(),
        "amenities": storage.all("Amenity").values()
    }
    return render_template("10-hbnb_filters.html", models=data)

@app.teardown_appcontext
def close_db(exception=None):
    """
    Executes after each request: Closes the current SQLAlchemy Session.
    """
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
