from flask_login import current_user, login_user, logout_user
from models import db, AuthUser, login_manager  # login_manager declared in models.init.py


# Authorise User
# user_dict requires user_name, email, password
def model_authorize(user_dict):
    # check to see if the user is already registered
    existing_user = AuthUser.query.filter_by(email=user_dict['email']).first()
    # if not, register them
    if existing_user is None:
        auth_user = AuthUser(
            name=user_dict['user_name'],
            email=user_dict['email']
        )
        # encrypt their password and add it to the authuser object
        auth_user.set_password(user_dict['password'])
        db.session.add(auth_user)
        db.session.commit()  # Create new user


# if login url, show phones table only
def model_login(user_dict):
    # Bypass if user is logged in
    if current_user.is_authenticated:
        return True
    # if not already logged in, show the login form
    print(user_dict['email'])
    user_record = AuthUser.query.filter_by(email=user_dict['email']).first()
    if user_record and AuthUser.check_password(user_record, user_dict['password']):
        login_user(user_record)
        return True
    # login failed
    return False


# logout user
def model_logout():
    logout_user()


# this function is needed for Flask-Login to work.
@login_manager.user_loader
def model_user_loader(user_id):
    """Check if user is logged-in on every page load."""
    if user_id is not None:
        return AuthUser.query.get(user_id)
    return None
