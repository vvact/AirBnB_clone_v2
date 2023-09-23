#!/usr/bin/python3
"""
Start a flask web application
listening on 0.0.0.0 port 5000
Routes: /, /hbnb. /c/<text>
"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """display Hello HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def variable_in_url(text):
    """Url with a variable"""
    text = text.replace('_', ' ')
    return f"C {text}"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
