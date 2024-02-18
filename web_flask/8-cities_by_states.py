#!/usr/bin/python3
"""a script that starts a flask web applications"""

from flask import Flask, render_template
from models import storage
from models.state import State

# it creates an instance of the Flask class and assigns it to app variable
app = Flask(__name__)


# teardown app context to remove the current
# sqlalchemy session after each repeat
@app.teardown_appcontext
def teardown(exception):
    """it removes the current sqlalchemy session"""
    storage.close()


# it defines the url that ends with /cities_by_states
@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """it displays an html page with a list of all state objects
    and related citiesin DBStorage. states/city are sorted by name
    """
    # this fetches all state objects from the DBStorage and sort them by name
    states = storage.all(State)
    return render_template("8-cities_by_states.html", states=states)


if __anme__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
