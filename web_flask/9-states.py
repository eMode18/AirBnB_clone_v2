#!/usr/bin/python3
"""
Code initiating a Flask web application:
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.route('/states', strict_slashes=False)
def states_list_route():
    """
    Route to display a list of states: Renders an HTML page
    presenting states sorted by name A->Z.
    Returns:
        html: Template showcasing all states sorted alphabetically by name
    """
    states = storage.all("State").values()
    return render_template("7-states_list.html", states=states)

@app.route('/states/<id>', strict_slashes=False)
def states_by_id_route(id):
    """
    Route to get a state by id: Renders an HTML page displaying cities of the
    state sorted by name A->Z.
    Returns:
        html: Template listing cities of the state, sorted alphabetically
        by name
    """
    state = None
    for s in storage.all("State").values():
        if s.id == id:
            state = s
            break
    return render_template("9-states.html", state=state)

@app.teardown_appcontext
def close_db(exception=None):
    """
    Executes after each request: Terminates the current SQLAlchemy Session.
    """
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

