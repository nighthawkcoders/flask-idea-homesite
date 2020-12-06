"""_init_.py is used to define app and all blueprints"""
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///models/myDB.db'
db = SQLAlchemy(app)


from pythondb import pythondb_bp
app.register_blueprint(pythondb_bp, url_prefix='/pythondb')