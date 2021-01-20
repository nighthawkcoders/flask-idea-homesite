"""__init__.py is used to define app and all blueprints"""
from flask import Flask
app = Flask(__name__)

""" blue prints """
from restapi import restapi_bp
from pythondb import pythondb_bp
app.register_blueprint(restapi_bp, url_prefix='/restapi')
app.register_blueprint(pythondb_bp, url_prefix='/pythondb')
