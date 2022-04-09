#!usr/bin/python3
"""
script listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: Displays 'HBNB'

"""
from flask import Flask
app = Flsk(__name__)



@app.route("/", strict_slashes=False)
def index():
    """displays Hellow HBNB!"""
        return "Hello HBNB!"



@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'HBNB'."""
    return "HBNB"



if __name__ == '__main__':
        app.run(host="0.0.0.0")
