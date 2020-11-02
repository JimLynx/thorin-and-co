import os
from flask import Flask


app = Flask(__name__)

"""
decorator - When we try to browse to the 
root directory, as indicated by the "/", 
then Flask triggers the index function 
underneath and returns the "Hello, World" text.
"""

@app.route("/")

def index():
    return "Hello, World"


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"), #default ip if no other port can be found
        port=int(os.environ.get("PORT", "5000")), #common port used by flask
        debug=True
    )
