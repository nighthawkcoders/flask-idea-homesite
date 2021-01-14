from models.lessons.java import *
from models.lessons.python import *
from models.lessons.pi import *
from models.lessons.git import *
from models.lessons.pbl import *

"""Dropdown data for menu selection"""
# This table is used to inform HTML of items to be placed in main menu
# -- data provider requirements are "title" and "key"
# ---- "title" is displayed in dropdown
# ---- "key" is used in building dynamic URL (https://www.tutorialspoint.com/flask/flask_variable_rules.htm)
menus = [
    java_details(),
    python_details(),
    pi_details(),
    git_details(),
    pbl_details()
]

"""dictionary that goes with menu selection"""
# This dictionary is used to obtain data associated with a dynamic URL
# -- The key looked up in the dictionary returns a list that has two elements
# ---- [0] the title associated to key, used for display on landing page
# ---- [1] the projects/choices associated to key, used to populate choices on landing page selector widget
TITLE = 0
PROJECTS = 1
select_2_proj = {
    java_details()['key']: [java_details()['title'], java_projects()],
    python_details()['key']: [python_details()['title'], python_projects()],
    pi_details()['key']: [pi_details()['title'], pi_projects()],
    git_details()['key']: [git_details()['title'], git_projects()],
    pbl_details()['key']: [pbl_details()['title'], pbl_projects()]
}

"""dictionary that maps key (route) with value (data) for project page"""
lessons_dict = { \
    java_ap()['route']: java_ap(),
    java_hello()['route']: java_hello(),
    java_mvc()['route']: java_mvc(),
    java_event()['route']: java_event(),
    java_study()['route']: java_study(),
    python_ap()['route']: python_ap(),
    python_hello()['route']: python_hello(),
    python_flask()['route']: python_flask(),
    python_cbproj()['route']: python_cbproj(),
    python_study()['route']: python_study(),
    python_database()['route']: python_database(),
    python_restapi()['route']: python_restapi(),
    pi_webserver()['route']: pi_webserver(),
    pi_deploy()['route']: pi_deploy(),
    pi_portforward()['route']: pi_portforward(),
    pi_realvnc()['route']: pi_realvnc(),
    pi_vncsetup()['route']: pi_vncsetup(),
    pi_ssh()['route']: pi_ssh(),
    git_concepts()['route']: git_concepts(),
    git_replto()['route']: git_replto(),
    pbl_overview()['route']: pbl_overview(),
    pbl_scrum()['route']: pbl_scrum(),
}
