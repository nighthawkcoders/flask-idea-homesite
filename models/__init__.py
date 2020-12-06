from models.java import java_details, java_projects
from models.python import  python_details, python_projects
from models.pi import pi_details, pi_projects
from models.git import git_details, git_projects
from models.pbl import pbl_details, pbl_projects

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
# This dictionary is used to obtain data associated with a dynamic URL
# -- The key looked up in the dictionary returns a list that has two elements
# ---- [0] the title associated to key, used for display on landing page
# ---- [1] the projects/choices associated to key, used to populate choices on landing page selector widget
TITLE = 0
PROJECTS = 1
key_2_proj = {java_details()['key']: [java_details()['title'], java_projects()],
              python_details()['key']: [python_details()['title'], python_projects()],
              pi_details()['key']: [pi_details()['title'], pi_projects()],
              git_details()['key']: [git_details()['title'], git_projects()],
              pbl_details()['key']: [pbl_details()['title'], pbl_projects()]}