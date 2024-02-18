#!/usr/bin/python3
"""a script that starts a flask web applications"""

from flask import Flask, render_template
app = Flask(__name__)


# defines the route for the root url '/'
@app.route('/', strict_slashes=False)
def display_hello_hbnb():
    """a func that returns Hello HBNB"""
    return "Hello HBNB!"


# defines the roure for the url ending with /hbnb
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ it displays the 'HBNB'"""
    return "HBNB"


# it handles the url the ends with /c/c_fun
@app.route('/c/<text>', strict_slashes=False)
def c_plus_text(text):
    """it displays c followed by the value in <text>"""
    text_formatted = text.replace("_", " ")
    return "C {}".format(text_formatted)


# it handles the url the ends with /python/<text>
@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_plus_text(text):
    """it displays python followed by the value in <text>"""
    text_formatted = text.replace("_", " ")
    return "Python {}".format(text_formatted)


# it handles the url the ends with /number/<n>
@app.route('/number/<int:n>', strict_slashes=False)
def ends_with_number(n):
    """it displays the value in n plus 'is a number' """
    return "{} is a number".format(n)


# it handles the url the ends with /number_template/<n>
@app.route('/number_template/<int:n>', strict_slashes=False)
def number_plus_template(n):
    """it displays a HTML page only if n is an integer"""
    return render_template("5-number.html", n=n)


if __name__ == '__main__':
    # this starts the flask development server and
    # listens on all available network interfaces(0.0.0.0) and prot 8000
    app.run(host='0.0.0.0', port=5000)
