#!/usr/bin/python3
"""a script that starts a flask web applications"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

# it creates an instance of the Flask class and assigns it to app variable
app = Flask(__name__)


# teardown app context to remove the current
# sqlalchemy session after each repeat
@app.teardown_appcontext
def teardown(exception):
    """it removes the current sqlalchemy session"""
    storage.close()


# it defines the url that ends with /cities_by_states
@app.route('/states', strict_slashes=False)
def states():
    """it displays a html page with a list of all states"""
    states = storage.all("state")
    render_template("9-states.html", state=states)


# it defines the url that ends with /states/<id>
@app.route('/states/<id>', strict_slashes=False)
def states_by_id(id):
    """it displays an html page about <id> if it exists
    """
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


if __anme__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
