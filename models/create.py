from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

app = Flask(__name__)

""" database locations """
dbURI = 'sqlite:///createDB'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
db = SQLAlchemy(app)

"""
Sample of table creation and data population
"""

"""DB creation"""
engine = create_engine(dbURI)
session = Session(bind=engine)


class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=False, nullable=False)
    nickname = db.Column(db.String(255), unique=False, nullable=False)
    email = db.Column(db.String(60), unique=True, key='email')

if __name__ == "__main__":
    """create each table"""
    db.create_all()
    try:
        u1 = Users(name='Thomas Edison', nickname='Toby', email='tedison@example.com')
        u2 = Users(name='Nicholas Tesla', nickname='Niko', email='ntesla@example.com')
        u3 = Users(name='Alexander Graham Bell', nickname='Lex', email='agbell@example.com')
        u4 = Users(name='Eli Whitney', nickname='Whit', email='eliw@example.com')
        session.add_all([u1, u2, u3, u4])
        session.commit()
    except:
        print("Records exist")

    print("Table: Users")
    list = Users.query.all()
    for row in list:
        print(row.user_id)
        print(row.name)
        print(row.nickname)
        print(row.email)

"""
Test on Terminal from IntelliJ
MacBook-Pro-2:flask-idea-homesiteZ johnmortensen$ cd models
MacBook-Pro-2:models johnmortensen$ sqlite3
SQLite version 3.32.3 2020-06-18 14:16:19
Enter ".help" for usage hints.
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persistent database.

sqlite> .open createDB
sqlite> .tables
users

sqlite> select * from users;
1|Thomas Edison|Toby|tedison@example.com
2|Nicholas Tesla|Niko|ntesla@example.com
3|Alexander Graham Bell|Lex|agbell@example.com
4|Eli Whitney|Whit|eliw@example.com
"""
