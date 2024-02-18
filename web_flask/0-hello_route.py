#!/usr/bin/python3
"""a script that starts a flask web applications"""

from flask import Flask
app = Flask(__name__)


# defines the route for the root url '/'
@app.route('/', strict_slashes=False)
def display_hello_hbnb():
    """a func that returns Hello HBNB"""
    return "Hello HBNB!"


if __name__ == '__main__':
    # this starts the flask development server and
    # listens on all available network interfaces(0.0.0.0) and prot 8000
    app.run(host='0.0.0.0', port=5000)
