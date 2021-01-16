from flask_sqlalchemy import SQLAlchemy
from __init__ import app

dbURI = 'sqlite:///models/myDB.db'

""" database setup to support db examples """
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
db = SQLAlchemy(app)

# declare the users database model
class Users(db.Model):
    UserID = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), unique=True, nullable=False)


# Declare emails database model
class Emails(db.Model):
    UserID = db.Column(db.Integer, primary_key=True)
    email_address = db.Column(db.String(255), unique=True, nullable=False)


# declare phone numbers database model
class PhoneNumbers(db.Model):
    UserID = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.String(255), unique=True, nullable=False)

