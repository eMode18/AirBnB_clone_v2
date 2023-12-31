#!/usr/bin/python3
"""
Code initiating a Flask web application:
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def states_list_route():
    """
    Route to display a list of states: Renders an HTML page presenting
    states sorted by name A->Z.
    Returns:
        html: Template showcasing all states sorted alphabetically by name
    """
    states = storage.all("State").values()
    return render_template("7-states_list.html", states=states)

@app.teardown_appcontext
def close_db(exception=None):
    """
    Executes after each request: Terminates the current SQLAlchemy Session.
    """
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
