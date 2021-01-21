from flask import render_template, request, redirect, url_for
from sqlalchemy import func
from views.pythondb import pythondb_bp
from models import db, Users, Emails, PhoneNumbers, AuthUser
from models.lessons import menus
from flask_login import current_user, login_user

# connects default URL to a function
@pythondb_bp.route('/')
def databases():
    """convert Users table into a list of dictionary rows"""
    records = []
    users = Users.query.all()
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
        """fetch userid"""
        userid = request.form.get("ID")
        """filter users by userid"""
        user = Users.query.filter_by(UserID=userid).first()
        user_dict = {'id': user.UserID, 'name': user.username, 'password': user.password}
        """filter email by userid"""
        email = Emails.query.filter_by(UserID=userid).first()
        if email:
            user_dict['emails'] = email.email_address
        """filter phone number by userid"""
        pn = PhoneNumbers.query.filter_by(UserID=userid).first()
        if pn:
            user_dict['phone_numbers'] = pn.phone_number
        """put filtered data into list form"""
        record = [user_dict]
    return render_template("pythondb/index.html", table=record, menus=menus)


# CRUD update
@pythondb_bp.route('/update/', methods=["POST"])
def update():
    if request.form:
        """fetch userid"""
        userid = request.form.get("ID")
        """update email in table from data in form if it exists, insert if not"""
        if Emails.query.filter_by(UserID=userid).first() is not None:
            db.session.query(Emails).filter_by(UserID=userid).update({Emails.email_address: request.form.get("email")})
        else:
            email = Emails(email_address=request.form.get("email"), UserID=userid)
            db.session.add(email)
        """update phone number in table from data in form"""
        if PhoneNumbers.query.filter_by(UserID=userid).first() is not None:
            db.session.query(PhoneNumbers).filter_by(UserID=userid).update(
                {PhoneNumbers.phone_number: request.form.get("phone_number")})
        else:
            phone_number = PhoneNumbers(phone_number=request.form.get("phone_number"), UserID=userid)
            db.session.add(phone_number)

        """commit changes to database"""
        db.session.commit()
    return redirect(url_for('pythondb_bp.databases'))


# CRUD delete
@pythondb_bp.route('/delete/', methods=["POST"])
def delete():
    if request.form:
        """fetch userid"""
        userid = request.form.get("ID")
        """delete userid rows from emails table"""
        db.session.query(Emails).filter(Emails.UserID == userid).delete()
        """delete userid rows from phone numbers table"""
        db.session.query(PhoneNumbers).filter(PhoneNumbers.UserID == userid).delete()
        """delete userid rows from users table"""
        db.session.query(Users).filter(Users.UserID == userid).delete()
        """commit changes to database"""
        db.session.commit()
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


# if auth user url, show phones table only
@pythondb_bp.route('/auth_user/', methods=["POST"])
def auth_user():
    # check form inputs and create auth user
    print("In auth_user")
    if request.form.get("txtUsername") is not None:
        print("UN: " + request.form.get("txtUsername"))
    else:
        print("UN: None")
    if request.form.get("txtUsername") != "" and request.form.get("txtUsername") is not None \
            and request.form.get("txtEmail") != "" and request.form.get("txtEmail") is not None \
            and request.form.get("txtPwd1.") != "" and request.form.get("txtPwd1.") is not None:
        existing_user = AuthUser.query.filter_by(email=request.form.get("txtEmail")).first()
        print("Username: " + request.form.get("txtUsername"))
        if existing_user is None:
            print("No exisiting user")
            authuser = AuthUser(
                name=request.form.get("txtUsername"),
                email=request.form.get("txtEmail")
            )
            print("New username: " + authuser.name)
        authuser.set_password(request.form.get("txtPwd1"))
        db.session.add(authuser)
        db.session.commit()  # Create new user
    # show the auth user page
    return render_template("pythondb/auth_user.html")


# if login url, show phones table only
@pythondb_bp.route('/login/', methods=["GET", "POST"])
def login():
    # Bypass if user is logged in
    if current_user.is_authenticated:
        return redirect(url_for('main_bp.dashboard'))

    if request.form.get("txtUsername") != "" and request.form.get("txtUsername") is not None \
            and request.form.get("txtEmail") != "" and request.form.get("txtEmail") is not None \
            and request.form.get("txtPwd1.") != "" and request.form.get("txtPwd1.") is not None:
        this_user = AuthUser.query.filter_by(email=request.form.get("txtEmail")).first()
        if this_user and AuthUser.check_password(password=request.form.get("txtPwd")):
            login_user(this_user)
            return redirect(url_for('pythondb_bp.logged_in'))

    # if not logged in, show the login page
    return render_template("pythondb_bp.auth_user")


"""
@pythondb_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.form.validate_on_submit():
        existing_user = auth_user.query.filter_by(email=form.email.data).first()
        if existing_user is None:
            authuser = auth_user(
                name=request.form.txtUsername,
                email=request.form.txtEmail
            )
        authuser.set_password(request.form.txtPwd)
        db.session.add(authuser)
        db.session.commit()  # Create new user
    return render_template("pythondb/auth_user.html")
"""
