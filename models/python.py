from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
from views import app


"""Model in MVC has responsibility of managing data or database"""

"""A series of dictionaries to support data rendering"""

""" PYTHON ONLY """


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///models/myDB.db'
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


def python_ap():
    group = "python"
    route = ".pythonap"
    title = "AP study big ideas outline"
    timeline = "https://padlet.com/embed/k3bwade11ekevmum"
    data = {"group": group, "route": route, "title": title, "timeline": timeline}
    return data


def python_databases():
    group = "python"
    route = ".databases"
    title = "Hello to Databases and Python"
    data = {"group": group, "route": route, "title": title}
    return data


def python_hello():
    group = "python"
    route = ".pythonhello"
    title = "Hello to Project-based learning and Python"
    timeline = "https://padlet.com/embed/2p9700yyoz3flccs"
    repo = "https://gh-card.dev/repos/nighthawkcoders/pythonhello.svg"
    repo_description = "Hello, World! and a variety of classroom and technical introductions"
    repl = "https://repl.it/@jmort1021/Python-Hello-Series?lite=true"
    data = {"group": group, "route": route, "title": title, "timeline": timeline, "repo": repo,
            "repo_description": repo_description, "repl": repl}
    return data


def python_flask():
    group = "python"
    route = ".pythonflask"
    title = "Flask Web server introduction and ideas"
    timeline = "https://padlet.com/embed/onshvns8f7vrrn2l"
    repo = "https://gh-card.dev/repos/nighthawkcoders/flask-idea-portfolio.svg?link_target=_blank"
    repo_description = "Ideas for building a Flask Web Server."
    repl = "https://repl.it/@jmort1021/Python-Web-Portfolio-Series?lite=true"
    data = {"group": group, "route": route, "title": title, "timeline": timeline, "repo": repo,
            "repo_description": repo_description, "repl": repl}
    return data


def python_cbproj():
    group = "python"
    route = ".pythoncbproj"
    title = "College Board project preparation focus"
    timeline = "https://padlet.com/jmortensen7/cspcbproject"
    repo = "https://gh-card.dev/repos/nighthawkcoders/flask-idea-homesite.svg?link_target=_blank"
    repo_description = "Start process of building a project for College Board. Use my website or previous projects as " \
                       "idea starters. "
    data = {"group": group, "route": route, "title": title, "timeline": timeline, "repo": repo,
            "repo_description": repo_description}
    return data


def python_study():
    group = "python"
    route = ".pythonstudy"
    title = "Python study resources"
    padlet = "https://padlet.com/jmortensen7/csp2021"
    data = {"group": group, "route": route, "title": title, "padlet": padlet}
    return data


def python_projects():
    return [python_hello(), python_flask(), python_cbproj(), python_ap(), python_study(), python_databases()]


def python_details():
    return {"title": 'CSP: Python', 'key': 'python'}
