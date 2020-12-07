from flask import render_template, request, redirect, url_for
from flask_table import Table, Col
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from pythondb import pythondb_bp
from pythondb.model import Users, Emails, PhoneNumbers
from models import menus
from __init__ import dbURI, db


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
        # filter email
        email = Emails.query.filter_by(UserID=user.UserID).first()
        if email:
            user_dict['emails'] = email.email_address
        # filter phone number
        pn = PhoneNumbers.query.filter_by(UserID=user.UserID).first()
        if pn:
            user_dict['phone_numbers'] = pn.phone_number
        # append to records
        records.append(user_dict)
    return render_template("pythondb/index.html", table=records, menus=menus)


# create/add a new record to the table
@pythondb_bp.route('/create/', methods=["POST"])
def create():
    if request.form:
        """prepare data for primary table extracting from form"""
        user = Users(username=request.form.get("username"), password=request.form.get("password"))
        """add and commit data to user table"""
        db.session.add(user)
        db.session.commit()
        """prepare data for related tables extracting from form and using new UserID """
        userid = db.session.query(func.max(Users.UserID))
        email = Emails(email_address=request.form.get("email"), UserID=userid)
        phone_number = PhoneNumbers(phone_number=request.form.get("phone_number"), UserID=userid)
        """email table add and commit"""
        db.session.add(email)
        db.session.commit()
        """phone number table add and commit"""
        db.session.add(phone_number)
        db.session.commit()
    return redirect(url_for('pythondb_bp.databases'))


# CRUD read, which is filtering table based off of ID
@pythondb_bp.route('/read/', methods=["POST"])
def read():
    if request.form:
        userid = request.form.get("ID")
        # filter user
        user = Users.query.filter_by(UserID=userid).first()
        user_dict = {'id': user.UserID, 'name': user.username, 'password': user.password}
        # filter email
        email = Emails.query.filter_by(UserID=userid).first()
        if email:
            user_dict['emails'] = email.email_address
        # filter phone number
        pn = PhoneNumbers.query.filter_by(UserID=userid).first()
        if pn:
            user_dict['phone_numbers'] = pn.phone_number
        # put record in list form
        record = [user_dict]
    return render_template("pythondb/index.html", table=record, menus=menus)


# CRUD update
@pythondb_bp.route('/update/', methods=["POST"])
def update():
    if request.form:
        userid = request.form.get("ID")
        engine = create_engine(dbURI, echo=True)  # relative path within project
        Session = sessionmaker(bind=engine)
        session = Session()
        session.query(Emails).filter_by(UserID=userid).update({Emails.email_address: request.form.get("email")})
        session.commit()
        session.query(PhoneNumbers).filter_by(UserID=userid).update(
            {PhoneNumbers.phone_number: request.form.get("phone_number")})
        session.commit()
    return redirect(url_for('pythondb_bp.databases'))


# CRUD delete
@pythondb_bp.route('/delete/', methods=["POST"])
def delete():
    if request.form:
        engine = create_engine(dbURI, echo=True)  # relative path within project
        Session = sessionmaker(bind=engine)
        session = Session()
        # userid = request.form.get("ID")
        session.query(Emails).filter(Emails.UserID == request.form.get("ID")).delete()
        session.commit()
        session.query(PhoneNumbers).filter(PhoneNumbers.UserID == request.form.get("ID")).delete()
        # phone = PhoneNumbers.query.filter_by(UserID=userid)
        # phone.phone_number = request.form.get("phone_number")
        session.commit()
    return redirect(url_for('pythondb_bp.databases'))


# if email url, show the email table only
@pythondb_bp.route('/emails/')
def emails():
    # fill the table with emails only
    records = []
    emails = Emails.query.all()
    for email in emails:
        user_dict = {}
        user_dict['id'] = email.UserID
        user_dict['emails'] = email.email_address
        records.append(user_dict)
    return render_template("pythondb/index.html", table=records, menu=menus)


# if phones url, show phones table only
@pythondb_bp.route('/phones/')
def phones():
    # fill the table with phone numbers only
    records = []
    phone_numbers = PhoneNumbers.query.all()
    for phone in phone_numbers:
        user_dict = {}
        user_dict['id'] = phone.UserID
        user_dict['phone_numbers'] = phone.phone_number
        records.append(user_dict)
    return render_template("pythondb/index.html", table=records, menu=menus)
