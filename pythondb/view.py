from flask import render_template
from flask_table import Table, Col
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pythondb import pythondb_bp
from pythondb.model import Users, Emails, PhoneNumbers
from models import menus


# Declare your Users table
class UserTable(Table):
    UserID = Col('UserID')
    username = Col('username')
    password = Col('Password')


# Declare your  emailtable
class EmailTable(Table):
    UserID = Col('UserID')
    email_address = Col('email_address')


# Declare your  phone numbers table
class PNTable(Table):
    UserID = Col('UserID')
    phone_number = Col('phone_number')


# connects default URL to a function
@pythondb_bp.route('/')
def databases():
    # fill the Users table
    users = Users.query.all()
    records = []
    for user in users:
        user_dict = {'id': user.UserID, 'name': user.username, 'password': user.password}
        # associate emails with user
        emails = Emails.query.all()
        for email in emails:
            if user_dict['id'] == email.UserID:
                user_dict['emails'] = email.email_address
        # associate phone numbers with user
        phone_numbers = PhoneNumbers.query.all()
        for pn in phone_numbers:
            if user_dict['id'] == pn.UserID:
                user_dict['phone_numbers'] = pn.phone_number
        # add record to list
        records.append(user_dict)
    return render_template("pythondb/PaulN.html", table=records, menus=menus)


# if input url used, use the input html
@pythondb_bp.route('/python/input/', methods=["GET", "POST"])
def input_route():
    if request.form:
        engine = create_engine('sqlite:///models/myDB.db', echo=True)  # relative path within project
        Session = sessionmaker(bind=engine)
        session = Session()
        print("UserID: " + str(request.form.get("ID")))
        email = Emails(email_address=request.form.get("email"), UserID=request.form.get("ID"))
        session.add(email)
        print(session)
        session.commit()
        phone_number = PhoneNumbers(phone_number=request.form.get("phone_number"), UserID=request.form.get("ID"))
        session.add(phone_number)
        session.commit()
    return render_template("pythondb/PaulN.html", menus=menus)


# if email url, show the email table
@pythondb_bp.route('/python/emails/')
def emails_route():
    # user = Users.query.filter_by(UserID=1).first()
    print("Emails")
    # fill the emails table object
    emails = Emails.query.all()
    emailTable = EmailTable(emails)
    for email in emails:
        print(str(email.UserID) + ' ' + email.email_address)
    return render_template("pythondb/PaulN.html", table=emailTable, menu=menus)


# if phones url, shjow phones table
@pythondb_bp.route('/python/phones/')
def phones_route():
    # user = Users.query.filter_by(UserID=1).first()
    print("Phone Numbers")
    # fill the phone numbers table object
    phone_numbers = PhoneNumbers.query.all()
    pntable = PNTable(phone_numbers)
    return render_template("pythondb/PaulN.html", table=pntable, menu=menus)
