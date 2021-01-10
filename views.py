"""Views in MVC has responsibility for establishing routes and redering HTML"""
from flask import render_template, request, redirect, url_for
from __init__ import app
from models.lessons import menus, TITLE, PROJECTS, select_2_proj, lessons_dict

"""Main navigation Section"""


# This section of code is driven by data, review data descriptions for understanding


@app.route('/')
def index():
    return render_template("homesite/home.html", menus=menus)


@app.route('/landing/<selection>/', methods=['GET', 'POST'])
def landing(selection):
    # POST redirection to content page
    if request.method == 'POST':
        form = request.form
        selection = form['page']
        try:    #allows for direct route
            return redirect(url_for(selection))
        except: #else the routes are handled by lesson select below
            return redirect(url_for("lesson", selection=selection))
    # GET landing page render based off of "selection"
    selected_list = select_2_proj[selection]  # selection is "key" used to pull project details from dictionary
    heading = selected_list[TITLE]
    projects = selected_list[PROJECTS]
    return render_template("homesite/landing.html", heading=heading, menus=menus, projects=projects)


"""Lesson Section"""


@app.route('/lesson/<selection>/')
def lesson(selection):
    return render_template("homesite/lesson.html", menus=menus, data=lessons_dict[selection])
