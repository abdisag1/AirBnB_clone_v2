#!usr/bin/python3
"""
script listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: Displays 'HBNB'.
/c/<text>: Displays 'C' followed by the value of <text>.
"""
from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def index():
    """displays Hellow HBNB!"""
    return "Hello HBNB!"
    
@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """displays HBNB"""
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Displays 'C' followed by the value of <text>."""
    text = text.replace("_", " ")
    return "C {}".format(text)

           
if __name__ == '__main__':
        app.run(host="0.0.0.0")
