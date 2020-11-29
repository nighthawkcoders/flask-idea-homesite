"""Views in MVC has responsibility for establishing routes and redering HTML"""
from flask import render_template, request, redirect, url_for
from __init__ import app
from models.java import java_ap, java_hello, java_mvc, java_event, java_study, java_details, java_projects
from models.python import python_hello, python_ap, python_flask, python_cbproj, python_study, python_details, \
    python_projects
from models.pi import pi_webserver, pi_portforward, pi_vncsetup, pi_realvnc, pi_ssh, pi_details, pi_projects
from models.git import git_concepts, git_replto, git_details, git_projects
from models.pbl import pbl_overview, pbl_scrum, pbl_details, pbl_projects

"""Main navigation Section"""
# This section of code is driven by data, review data descriptions for understanding

"""Dropdown data for menu selection"""
# This table is used to inform HTML of items to be placed in main menu
# -- data provider requirements are "title" and "key"
# ---- "title" is displayed in dropdown
# ---- "key" is used in building dynamic URL (https://www.tutorialspoint.com/flask/flask_variable_rules.htm)
menus = [java_details(),
         python_details(),
         pi_details(),
         git_details(),
         pbl_details()
         ]

"""Coordinated lookup for dictionary that goes with selection"""
# This dictionary is used to obtain data associated with dynamic URL
# -- The key returns a list that has two elements
# ---- [0] the title
# ---- [1] the data to drive project selection dialog
TITLE=0
PROJECTS=1
data = {java_details()['key']: [java_details()['title'], java_projects()],
        python_details()['key']: [python_details()['title'], python_projects()],
        pi_details()['key']: [pi_details()['title'], pi_projects()],
        git_details()['key']: [git_details()['title'], git_projects()],
        pbl_details()['key']: [pbl_details()['title'], pbl_projects()]}


@app.route('/')
def index():
    return render_template("homesite/home.html", menus=menus)


@app.route('/landing/<selection>', methods=['GET', 'POST'])
def landing(selection):
    if request.method == 'POST':  # redirection to content page
        form = request.form
        page = form['page']
        return redirect(url_for(page))
    # based off of menu selection, content is selected for landing page
    select_list = data[selection]
    heading = select_list[TITLE]
    projects = select_list[PROJECTS]
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
