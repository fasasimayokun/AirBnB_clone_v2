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


# it handles the url ending with /states
@app.route("/states", strict_slashes=False)
def states():
    """Displays a HTML page with the states"""
    states = storage.all("State")
    return render_template("9-states.html", state=states)


# it handles the url ending with /states/<id>
@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """Displays a HTML page with the state's id"""
    states = storage.all("State")
    for state in states.values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
