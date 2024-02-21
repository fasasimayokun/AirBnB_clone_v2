#!/usr/bin/python3
"""a script that starts a flask web applications"""

from flask import Flask, render_template
from models import storage
from models.state import State
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)


# it defines the url that ends with /states_list
@app.route('/states_list', strict_slashes=False)
def states_list():
    """it displays an html page with a list of all state objects
    in DBStorage. states are sorted by name
    """
    # this fetches all state objects from the DBStorage and sort them by name
    states = sorted(list(storage.all("State").values()), key=lambda st: st.name)
    return render_template("7-states_list.html", states=states)


# teardown app context to remove the current
# sqlalchemy session after each repeat
@app.teardown_appcontext
def teardown(exception):
    """it removes the current sqlalchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
