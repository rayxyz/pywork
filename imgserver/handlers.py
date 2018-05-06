#!/usr/bin/env python

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/hi")
def say_hi():
    return "Hi, the beautiful world!"

if __name__ == "__main__":
    app.run()