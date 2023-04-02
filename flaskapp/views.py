from flask import Flask
from flask import render_template
from datetime import datetime
from . import app

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/success/")
def success():
    return render_template("success.html")

@app.route("/form/")
def form():
    return render_template("form.html")
