"""Views in MVC has responsibility for establishing routes and redering HTML"""
from flask import render_template
from __init__ import app
from models import java_ap, java_hello, java_mvc, python_ap, python_flask, python_hello

# This table is used to inform HTML of primary menu items and routes
menus = [{"title": 'Java', "route": '.java'},
         {"title": 'Python', "route": '.python'},
         {"title": 'About', "route": '.about'}]

@app.route('/')
def index():
    return render_template("homesite/home.html", menus=menus)


@app.route('/java')
def java():
    return render_template("homesite/java.html", menus=menus)


@app.route('/java/hello')
def javahello():
    return render_template("homesite/project.html", menus=menus, data=java_hello())


@app.route('/java/mvc')
def javamvc():
    return render_template("homesite/project.html", menus=menus, data=java_mvc())


@app.route('/java/ap')
def javaap():
    return render_template("homesite/project.html", menus=menus, data=java_ap())


@app.route('/python')
def python():
    return render_template("homesite/python.html", menus=menus)


@app.route('/python/hello')
def pythonhello():
    return render_template("homesite/project.html", menus=menus, data=python_hello())


@app.route('/python/flask')
def pythonflask():
    return render_template("homesite/project.html", data=python_flask())


@app.route('/python/ap')
def pythonap():
    return render_template("homesite/project.html", menus=menus, data=python_ap())


@app.route('/about')
def about():
    return render_template("homesite/about.html", menus=menus)
