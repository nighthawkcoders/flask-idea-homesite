from flask import render_template

from __init__ import app

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/java')
def java():
    return render_template("java.html")

@app.route('/python')
def python():
    return render_template("python.html")

@app.route('/about')
def about():
    return render_template("about.html")
