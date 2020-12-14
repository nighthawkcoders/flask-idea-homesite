from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, inspect

app = Flask(__name__)

''' database setup  '''
dbURI = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
db = SQLAlchemy(app)

''' table definitions '''


class user(db.Model):
    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    pasword = db.Column(db.String(255), unique=True, nullable=False)


class emails(db.Model):
    email_id = db.Column(db.Integer, primary_key=True)
    email_address = db.Column(db.String(255), unique=True, nullable=False)
    userid = db.Column(db.Integer, db.ForeignKey('user.userid'))


class phone_numbers(db.Model):
    phone_id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.String(255), unique=True, nullable=False)
    userid = db.Column(db.Integer, db.ForeignKey('user.userid'))

    def __repr__(self):
        return '<User %r>' % self.username


''' table creation '''
db.create_all()

''' inspect table '''
engine = create_engine(dbURI)
insp = inspect(engine)
for name in insp.get_table_names():
    print("Table " + str(name))
