"""Views in MVC has responsibility for establishing routes and redering HTML"""
from flask import render_template
from __init__ import app
from models import java_ap, java_hello, java_mvc, java_event, java_study, java_projects
from models import python_hello, python_ap, python_flask, python_study, python_projects

"""Dropdown Section"""
# This table is used to inform HTML of primary menu items and routes
menus = [{"title": 'Java', "route": '.java'},
         {"title": 'Python', "route": '.python'},
         {"title": 'Git', "route": '.git'},
         {"title": 'Pi', "route": '.pi'},
         {"title": 'Scrum', "route": '.scrum'},
         {"title": 'About', "route": '.about'}]


@app.route('/')
def index():
    return render_template("homesite/home.html", menus=menus)


@app.route('/java')
def java():
    return render_template("homesite/landing.html", heading="Java", menus=menus, projects=java_projects())


@app.route('/python')
def python():
    return render_template("homesite/landing.html", heading="Python", menus=menus, projects=python_projects())



@app.route('/git')
def git():
    return render_template("homesite/git.html", menus=menus)


@app.route('/pi')
def pi():
    return render_template("homesite/pi.html", menus=menus)


@app.route('/scrum')
def scrum():
    return render_template("homesite/scrum.html", menus=menus)


@app.route('/about')
def about():
    return render_template("homesite/about.html", menus=menus)


"""Java Section"""


@app.route('/java/hello')
def javahello():
    return render_template("homesite/project.html", menus=menus, data=java_hello())


@app.route('/java/mvc')
def javamvc():
    return render_template("homesite/project.html", menus=menus, data=java_mvc())


@app.route('/java/ap')
def javaap():
    return render_template("homesite/project.html", menus=menus, data=java_ap())


@app.route('/java/event')
def javaevent():
    return render_template("homesite/project.html", menus=menus, data=java_event())


@app.route('/java/study')
def javastudy():
    return render_template("homesite/project.html", menus=menus, data=java_study())


"""Python Section"""


@app.route('/python/hello')
def pythonhello():
    return render_template("homesite/project.html", menus=menus, data=python_hello())


@app.route('/python/flask')
def pythonflask():
    return render_template("homesite/project.html", menus=menus, data=python_flask())


@app.route('/python/ap')
def pythonap():
    return render_template("homesite/project.html", menus=menus, data=python_ap())


@app.route('/python/study')
def pythonstudy():
    return render_template("homesite/project.html", menus=menus, data=python_study())
