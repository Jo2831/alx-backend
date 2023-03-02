#!/usr/bin/python3
"""
file 0-app
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    """desplay the index file"""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(debug=True)
