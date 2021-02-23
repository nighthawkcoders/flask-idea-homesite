# standard flask view support
from views.pythondb import pythondb_bp
from flask import render_template, request, redirect, url_for
# session and database support
from flask_login import login_required
from models import login_manager
from models.lessons import menus
from models.crud import model_create, model_read, model_update, model_delete, model_query_all, model_query_emails, \
    model_query_phones, temps_query_count, temps_query_max, temps_query_min, temps_query_meanhigh, temps_query_meanlow, \
    temps_query_table
from models.login import model_authorize, model_login, model_logout


# def register(fm_request):
@pythondb_bp.route('/temps/', methods=["GET", "POST"])
def temps():
    if request.form.get("txtCity") is not None:
        city = request.form.get("txtCity")
    else:
        city = ''
    count = temps_query_count()         # gets the count of records for this filtered set, and sets the module variable
    maxt = temps_query_max()            # gets the maximum temp in the filtered set
    mint = temps_query_min()            # gets the minimum temp in the filtered set
    meanh = temps_query_meanhigh()      # gets the mean high temp in the filtered set
    meanl = temps_query_meanlow()       # gets the mean low temp in the filtered set
    table = temps_query_table()         # gets the table of data
    return render_template('pythondb/temps.html', count=count, maxt=maxt, mint=mint, meanh=meanh, meanl=meanl, city=city, table=table)


# connects default URL to a function
@pythondb_bp.route('/')
def databases():
    """convert Users table into a list of dictionary rows"""
    records = model_query_all()
    return render_template("pythondb/index.html", table=records, menus=menus)


# create/add a new record to the table
@pythondb_bp.route('/create/', methods=["POST"])
def create():
    if request.form:
        """extract data from form"""
        user_dict = {'username': request.form.get("username"), 'password': request.form.get("password"),
                     'email': request.form.get("email"), 'phone_number': request.form.get("phone_number")}
        # model_create expects: username, password, email, phone_number
        model_create(user_dict)
    return redirect(url_for('pythondb_bp.databases'))


# CRUD read, which is filtering table based off of ID
@pythondb_bp.route('/read/', methods=["POST"])
def read():
    record = []
    if request.form:
        userid = request.form.get("ID")
        # model_read expects userid
        user_dict = model_read(userid)
        # model_read returns: username, password, email, phone_number
        record = [user_dict]  # placed in list for compatibility with index.html
    return render_template("pythondb/index.html", table=record, menus=menus)


# CRUD update
@pythondb_bp.route('/update/', methods=["POST"])
def update():
    if request.form:
        user_dict = {
            'userid': request.form.get("ID"),
            'email': request.form.get("email"),
            'phone_number': request.form.get("phone_number")
        }
        # model_update expects userid, email, phone_number
        model_update(user_dict)
    return redirect(url_for('pythondb_bp.databases'))


# CRUD delete
@pythondb_bp.route('/delete/', methods=["POST"])
def delete():
    if request.form:
        """fetch userid"""
        userid = request.form.get("ID")
        model_delete(userid)
    return redirect(url_for('pythondb_bp.databases'))


# if email url, show the email table only
@pythondb_bp.route('/emails/')
def emails():
    # fill the table with emails only
    records = model_query_emails()
    return render_template("pythondb/index.html", table=records, menu=menus)


# if phones url, show phones table only
@pythondb_bp.route('/phones/')
def phones():
    # fill the table with phone numbers only
    records = model_query_phones()
    return render_template("pythondb/index.html", table=records, menu=menus)


# Authorise User Section
# if auth user is the signup section
# the public page does not include @login_required
@pythondb_bp.route('/public/')
def public():
    return render_template("pythondb/public_page.html")


@pythondb_bp.route('/auth_user/', methods=["GET", "POST"])
def auth_user():
    # check form inputs and create auth user
    if request.form:
        # validation should be in HTML
        user_dict = {
            'user_name': request.form.get("txtUsername"),
            'email': request.form.get("txtEmail"),
            'password': request.form.get("txtPwd1")
        }
        # model_authorize requires user_dict: user_name, email, password
        model_authorize(user_dict)
        return redirect(url_for('pythondb_bp.login'))
    # show the auth user page if the above fails for some reason
    return render_template("pythondb/auth_user.html")


# if login url, show phones table only
@pythondb_bp.route('/login/', methods=["GET", "POST"])
def login():
    if request.form:
        # validation should be in HTML
        user_dict = {
            'user_name': request.form.get("txtUsername"),
            'email': request.form.get("txtEmail"),
            'password': request.form.get("txtPwd1")
        }
        if model_login(user_dict):
            return redirect(url_for('pythondb_bp.dashboard'))

    # if not logged in, show the login page
    return render_template("pythondb/login.html")


# logged in users can see the dashboard
@pythondb_bp.route('/dashboard/')
@login_required  # this is the code that Flask-Login uses to stop non logged in users
def dashboard():
    return render_template("pythondb/dashboard.html")


# give users a way to log out
@pythondb_bp.route("/logout")
@login_required
def logout():
    """User log-out logic."""
    model_logout()
    return redirect(url_for('pythondb_bp.login'))


# this code lets Flask-Login take unauthorised users back to the login page
@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    return redirect(url_for('pythondb_bp.login'))
