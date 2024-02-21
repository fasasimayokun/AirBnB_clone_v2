#!/usr/bin/python3
"""a script that starts a flask web applications"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

# it creates an instance of the Flask class and assigns it to app variable
app = Flask(__name__)


# teardown app context to remove the current
# sqlalchemy session after each repeat
@app.teardown_appcontext
def teardown(exception):
    """it removes the current sqlalchemy session"""
    storage.close()


# it defines the url that ends with /hbnb_filters
@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """display a HTML page like 6-index.html from static"""
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
