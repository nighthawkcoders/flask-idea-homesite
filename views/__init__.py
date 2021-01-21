"""Views in MVC has responsibility for establishing routes and redering HTML"""
from flask import render_template, request, redirect, url_for
from models.lessons import menus, TITLE, PROJECTS, select_2_proj, lessons_dict
import requests
from control import app
from views.restapi import restapi_bp
from views.pythondb import pythondb_bp

"""Defining routes"""
app.register_blueprint(restapi_bp, url_prefix='/restapi')
app.register_blueprint(pythondb_bp, url_prefix='/pythondb')


"""Main navigation section"""

@app.route('/')
def index():
    return render_template("homesite/index.html", menus=menus)


@app.route('/landing/<selection>/', methods=['GET', 'POST'])
def landing(selection):
    # POST redirection to content page
    if request.method == 'POST':
        form = request.form
        selection = form['page']
        try:  # allows for direct route
            return redirect(url_for(selection))
        except:  # else the routes are handled by lesson select below
            return redirect(url_for("lesson", selection=selection))
    # GET landing page render based off of "selection"
    selected_list = select_2_proj[selection]  # selection is "key" used to pull project details from dictionary
    heading = selected_list[TITLE]
    projects = selected_list[PROJECTS]
    return render_template("homesite/landing.html", heading=heading, menus=menus, projects=projects)


"""Lesson Section"""


@app.route('/lesson/<selection>/')
def lesson(selection):
    x = requests.get('https://w3schools.com/python/demopage.htm')
    print(x.text)
    return render_template("homesite/lesson.html", menus=menus, data=lessons_dict[selection])
