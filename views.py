"""Views in MVC has responsibility for establishing routes and redering HTML"""
from flask import render_template
from __init__ import app
from models import java_ap, java_hello, java_mvc

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/java')
def java():
    return render_template("java.html")

@app.route('/java/hello')
def javahello():
    return render_template("project.html", data=java_hello())

@app.route('/java/mvc')
def javamvc():
    return render_template("project.html", data=java_mvc())

@app.route('/java/ap')
def javaap():
    return render_template("project.html", data=java_ap())

@app.route('/python')
def python():
    return render_template("python.html")

@app.route('/about')
def about():
    return render_template("about.html")