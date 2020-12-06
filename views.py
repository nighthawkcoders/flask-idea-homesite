"""Views in MVC has responsibility for establishing routes and redering HTML"""
from flask import render_template, request, redirect, url_for
from __init__ import app
from models import menus, TITLE, PROJECTS, key_2_proj
from models.java import java_ap, java_hello, java_mvc, java_event, java_study
from models.python import python_hello, python_ap, python_flask, python_cbproj, python_study
from models.pi import pi_webserver, pi_portforward, pi_vncsetup, pi_realvnc, pi_ssh
from models.git import git_concepts, git_replto
from models.pbl import pbl_overview, pbl_scrum

"""Main navigation Section"""
# This section of code is driven by data, review data descriptions for understanding


@app.route('/')
def index():
    return render_template("homesite/home.html", menus=menus)


@app.route('/landing/<selection>', methods=['GET', 'POST'])
def landing(selection):
    # POST redirection to content page
    if request.method == 'POST':
        form = request.form
        page = form['page']
        return redirect(url_for(page))
    # GET landing page render based off of "selection"
    selected_list = key_2_proj[selection] # selection is "key" used to pull project details from dictionary
    heading = selected_list[TITLE]
    projects = selected_list[PROJECTS]
    return render_template("homesite/landing.html", heading=heading, menus=menus, projects=projects)


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


@app.route('/python/cbproj')
def pythoncbproj():
    return render_template("homesite/project.html", menus=menus, data=python_cbproj())


@app.route('/python/ap')
def pythonap():
    return render_template("homesite/project.html", menus=menus, data=python_ap())


@app.route('/python/study')
def pythonstudy():
    return render_template("homesite/project.html", menus=menus, data=python_study())


"""Git Section"""


@app.route('/git/concepts')
def gitconcepts():
    return render_template("homesite/project.html", menus=menus, data=git_concepts())


@app.route('/git/replto')
def gitreplto():
    return render_template("homesite/project.html", menus=menus, data=git_replto())


"""Pi Section"""


@app.route('/pi/webserver')
def piwebserver():
    return render_template("homesite/project.html", menus=menus, data=pi_webserver())


@app.route('/pi/portforward')
def piportforward():
    return render_template("homesite/project.html", menus=menus, data=pi_portforward())


@app.route('/pi/vncsetup')
def pivncsetup():
    return render_template("homesite/project.html", menus=menus, data=pi_vncsetup())


@app.route('/pi/realvnc')
def pirealvnc():
    return render_template("homesite/project.html", menus=menus, data=pi_realvnc())


@app.route('/pi/ssh')
def pissh():
    return render_template("homesite/project.html", menus=menus, data=pi_ssh())


"""PBL Section"""


@app.route('/pbl/overview')
def pbloverview():
    return render_template("homesite/project.html", menus=menus, data=pbl_overview())


@app.route('/pbl/scrum')
def pblscrum():
    return render_template("homesite/project.html", menus=menus, data=pbl_scrum())
