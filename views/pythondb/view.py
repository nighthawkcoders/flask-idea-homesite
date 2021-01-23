from views.pythondb import pythondb_bp
from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_user, login_required, logout_user
from sqlalchemy import func
from models import db, Users, Emails, PhoneNumbers, AuthUser, login_manager  # login_manager declared in models.init.py
from models.lessons import menus

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


# Authorise User Section
# if auth user is the signup section
@pythondb_bp.route('/auth_user/', methods=["GET", "POST"])
def auth_user():
    # check form inputs and create auth user
    if request.form.get("txtUsername") != "" and request.form.get("txtUsername") is not None \
            and request.form.get("txtEmail") != "" and request.form.get("txtEmail") is not None \
            and request.form.get("txtPwd1") != "" and request.form.get("txtPwd1") is not None:
        # check to see if the user is already registered
        existing_user = AuthUser.query.filter_by(email=request.form.get("txtEmail")).first()
        # if not, register them
        if existing_user is None:
            authuser = AuthUser(
                name=request.form.get("txtUsername"),
                email=request.form.get("txtEmail")
            )
            # encrypt their password and add it to the authuser object
            authuser.set_password(request.form.get("txtPwd1"))
            db.session.add(authuser)
            db.session.commit()  # Create new user
            # and have them log in
            return redirect(url_for('pythondb_bp.login'))
        else:
            # if already registered, have them log in
            return redirect(url_for('pythondb_bp.login'))
    # show the auth user page if the above fails for some reason
    return render_template("pythondb/auth_user.html")


# if login url, show phones table only
@pythondb_bp.route('/login/', methods=["GET", "POST"])
def login():
    # Bypass if user is logged in
    if current_user.is_authenticated:
        return redirect(url_for('pythondb_bp.dashboard'))
    # if not already logged in, show the login form
    if request.form.get("txtUsername") != "" and request.form.get("txtUsername") is not None:
        this_user = AuthUser.query.filter_by(email=request.form.get("txtEmail")).first()
        if this_user and AuthUser.check_password(this_user, password=request.form.get("txtPwd1")):
            login_user(this_user)
            return redirect(url_for('pythondb_bp.dashboard'))

    # if not logged in, show the login page
    return render_template("pythondb/login.html")


# logged in users can see the dashboard
@pythondb_bp.route('/dashboard/')
@login_required # this is the code that Flask-Login uses to stop non logged in users
def dashboard():
    return render_template("pythondb/dashboard.html")


# the public page does not include @login_required
@pythondb_bp.route('/public/')
def public():
    return render_template("pythondb/public_page.html")


# give users a way to log out
@pythondb_bp.route("/logout")
@login_required
def logout():
    """User log-out logic."""
    logout_user()
    return redirect(url_for('pythondb_bp.auth_user'))


# this function is needed for Flask-Login to work.
@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""
    if user_id is not None:
        return AuthUser.query.get(user_id)
    return None


# this code lets Flask-Login take unauthorised users back to the login page
@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    return redirect(url_for('pythondb_bp.login'))

