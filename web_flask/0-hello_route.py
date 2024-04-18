#!/usr/bin/python3
<<<<<<< HEAD
"""
start Flask application
=======
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
>>>>>>> 71d5fd3102f34dc8954eccd13e2d3b9421efd24a
"""
from flask import Flask

app = Flask(__name__)


<<<<<<< HEAD
@app.route('/', strict_slashes=False)
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
=======
@app.route("/airbnb-onepage", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
>>>>>>> 71d5fd3102f34dc8954eccd13e2d3b9421efd24a
