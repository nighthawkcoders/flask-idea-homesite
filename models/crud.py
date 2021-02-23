from sqlalchemy import func
from models import db, Users, Emails, PhoneNumbers, Temps
from flask import request
import my_module as m

m.fullCount = 0  # this is a module wide variable - can be seen within all functions


# CRUD create/add a new record to the table
# user_dict{} expects username, password, email, phone_number
def model_create(user_dict):
    """prepare data for primary table extracting from form"""
    user = Users(username=user_dict["username"], password=user_dict["password"])
    """add and commit data to user table"""
    db.session.add(user)
    db.session.commit()
    """prepare data for related tables extracting from form and using new UserID """
    userid = db.session.query(func.max(Users.UserID))
    email = Emails(email_address=user_dict["email"], UserID=userid)
    phone_number = PhoneNumbers(phone_number=user_dict["phone_number"], UserID=userid)
    """email table add and commit"""
    db.session.add(email)
    db.session.commit()
    """phone number table add and commit"""
    db.session.add(phone_number)
    db.session.commit()


# CRUD read: filter single record in table based off of userid
# userid required
def model_read(userid):
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
    return user_dict


# CRUD update
# user_dict{} expects userid, email, phone_number
def model_update(user_dict):
    """fetch userid"""
    userid = user_dict["userid"]
    """update email in table from data in form if it exists, insert if not"""
    if Emails.query.filter_by(UserID=userid).first() is not None:
        db.session.query(Emails).filter_by(UserID=userid).update({Emails.email_address: user_dict["email"]})
    else:
        email = Emails(email_address=user_dict["email"], UserID=userid)
        db.session.add(email)
    """update phone number in table from data in form"""
    if PhoneNumbers.query.filter_by(UserID=userid).first() is not None:
        db.session.query(PhoneNumbers).filter_by(UserID=userid).update(
            {PhoneNumbers.phone_number: user_dict["phone_number"]})
    else:
        phone_number = PhoneNumbers(phone_number=user_dict["phone_number"], UserID=userid)
        db.session.add(phone_number)

    """commit changes to database"""
    db.session.commit()


# CRUD delete
# userid required
def model_delete(userid):
    """fetch userid"""
    userid = userid
    """delete userid rows from emails table"""
    db.session.query(Emails).filter(Emails.UserID == userid).delete()
    """delete userid rows from phone numbers table"""
    db.session.query(PhoneNumbers).filter(PhoneNumbers.UserID == userid).delete()
    """delete userid rows from users table"""
    db.session.query(Users).filter(Users.UserID == userid).delete()
    """commit changes to database"""
    db.session.commit()


# CRUD read: query all tables and records in the table
def model_query_all():
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
    return records


# CRUD read: query emails table
def model_query_emails():
    # fill the table with emails only
    records = []
    emails = Emails.query.all()
    for email in emails:
        user_dict = {'id': email.UserID, 'emails': email.email_address}
        records.append(user_dict)
    return records


# CRUD read: query phones table
def model_query_phones():
    # fill the table with phone numbers only
    records = []
    phone_numbers = PhoneNumbers.query.all()
    for phone in phone_numbers:
        user_dict = {'id': phone.UserID, 'phone_numbers': phone.phone_number}
        records.append(user_dict)
    return records


# TEMPS count: filter the temps as required, and return the count of the records
def temps_query_count():
    my_filters = {}
    if request.form.get("txtCity") != '' and request.form.get("txtCity") is not None:
        my_filters["City"] = request.form.get("txtCity")
    if request.form.get("txtMin") != '' and request.form.get("txtMin") is not None:
        my_filters["MinTemp"] = int(request.form.get("txtMin"))
    if request.form.get("txtMax") != '' and request.form.get("txtMax") is not None:
        my_filters["MaxTemp"] = int(request.form.get("txtMax"))
    if request.form.get("txtDate") != '' and request.form.get("txtDate") is not None:
        my_filters["DateRecorded"] = str(request.form.get("txtDate"))
    query = db.session.query(Temps)
    for attr, value in my_filters.items():
        if attr == "MinTemp":
            query = query.filter(getattr(Temps, attr) >= value)
        else:
            if attr == "MaxTemp":
                query = query.filter(getattr(Temps, attr) <= value)
            else:
                query = query.filter(getattr(Temps, attr) == value)
    print("Fil: " + str(my_filters))
    count = query.count()
    m.fullCount = count  # module wide variable set here
    return count


# TEMPS Max Temp query
def temps_query_max():
    my_filters = {}
    if request.form.get("txtCity") != '' and request.form.get("txtCity") is not None:
        my_filters["City"] = request.form.get("txtCity")
    if request.form.get("txtMin") != '' and request.form.get("txtMin") is not None:
        my_filters["MinTemp"] = int(request.form.get("txtMin"))
    if request.form.get("txtMax") != '' and request.form.get("txtMax") is not None:
        my_filters["MaxTemp"] = int(request.form.get("txtMax"))
    if request.form.get("txtDate") != '' and request.form.get("txtDate") is not None:
        my_filters["DateRecorded"] = str(request.form.get("txtDate"))
    query = db.session.query(func.max(Temps.MaxTemp))
    for attr, value in my_filters.items():
        if attr == "MinTemp":
            query = query.filter(getattr(Temps, attr) >= value)
        else:
            if attr == "MaxTemp":
                query = query.filter(getattr(Temps, attr) <= value)
            else:
                query = query.filter(getattr(Temps, attr) == value)

    print("Fil: " + str(my_filters))
    if m.fullCount != 0:  # this ensures there are results in this filtered set
        myresult = query.first()
        strResult = extract_value(str(myresult))
        maxtemp = int(strResult)
    else:
        maxtemp = 0
    return maxtemp


# TEMPS Min Temp query
def temps_query_min():
    my_filters = {}
    if request.form.get("txtCity") != '' and request.form.get("txtCity") is not None:
        my_filters["City"] = request.form.get("txtCity")
    if request.form.get("txtMin") != '' and request.form.get("txtMin") is not None:
        my_filters["MinTemp"] = int(request.form.get("txtMin"))
    if request.form.get("txtMax") != '' and request.form.get("txtMax") is not None:
        my_filters["MaxTemp"] = int(request.form.get("txtMax"))
    if request.form.get("txtDate") != '' and request.form.get("txtDate") is not None:
        my_filters["DateRecorded"] = str(request.form.get("txtDate"))
    query = db.session.query(func.min(Temps.MinTemp))
    for attr, value in my_filters.items():
        if attr == "MinTemp":
            query = query.filter(getattr(Temps, attr) >= value)
        else:
            if attr == "MaxTemp":
                query = query.filter(getattr(Temps, attr) <= value)
            else:
                query = query.filter(getattr(Temps, attr) == value)
    # count = db.engine.execute('select count(id) from temps').scalar()
    if m.fullCount != 0:  # this ensures there are results in this filtered set
        myresult = query.first()
        strResult = extract_value(str(myresult))
        mintemp = int(strResult)
    else:
        mintemp = 0
    return mintemp


# TEMPS mean Hign Temp query
def temps_query_meanhigh():
    my_filters = {}
    if request.form.get("txtCity") != '' and request.form.get("txtCity") is not None:
        my_filters["City"] = request.form.get("txtCity")
    if request.form.get("txtMin") != '' and request.form.get("txtMin") is not None:
        my_filters["MinTemp"] = int(request.form.get("txtMin"))
    if request.form.get("txtMax") != '' and request.form.get("txtMax") is not None:
        my_filters["MaxTemp"] = int(request.form.get("txtMax"))
    if request.form.get("txtDate") != '' and request.form.get("txtDate") is not None:
        my_filters["DateRecorded"] = str(request.form.get("txtDate"))
    query = db.session.query(func.avg(Temps.MaxTemp))
    for attr, value in my_filters.items():
        if attr == "MinTemp":
            query = query.filter(getattr(Temps, attr) >= value)
        else:
            if attr == "MaxTemp":
                query = query.filter(getattr(Temps, attr) <= value)
            else:
                query = query.filter(getattr(Temps, attr) == value)
    # count = db.engine.execute('select count(id) from temps').scalar()
    print("Fil: " + str(my_filters))
    if m.fullCount != 0:  # this ensures there are results in this filtered set
        myresult = query.first()
        strResult = extract_value(str(myresult))
        meanhigh = round(float(strResult), 2)
    else:
        meanhigh = 0

    return meanhigh


# TEMPS mean low Temp query
def temps_query_meanlow():
    my_filters = {}
    if request.form.get("txtCity") != '' and request.form.get("txtCity") is not None:
        my_filters["City"] = request.form.get("txtCity")
    if request.form.get("txtMin") != '' and request.form.get("txtMin") is not None:
        my_filters["MinTemp"] = int(request.form.get("txtMin"))
    if request.form.get("txtMax") != '' and request.form.get("txtMax") is not None:
        my_filters["MaxTemp"] = int(request.form.get("txtMax"))
    if request.form.get("txtDate") != '' and request.form.get("txtDate") is not None:
        my_filters["DateRecorded"] = str(request.form.get("txtDate"))
    query = db.session.query(func.avg(Temps.MinTemp))
    for attr, value in my_filters.items():
        if attr == "MinTemp":
            query = query.filter(getattr(Temps, attr) >= value)
        else:
            if attr == "MaxTemp":
                query = query.filter(getattr(Temps, attr) <= value)
            else:
                query = query.filter(getattr(Temps, attr) == value)
    # count = db.engine.execute('select count(id) from temps').scalar()
    print("Fil: " + str(my_filters))
    if m.fullCount != 0:  # this ensures there are results in this filtered set
        myresult = query.first()
        strResult = extract_value(str(myresult))
        meanlow = round(float(strResult), 2)
    else:
        meanlow = 0
    return meanlow

def temps_query_table():
    my_filters = {}
    if request.form.get("txtCity") != '' and request.form.get("txtCity") is not None:
        my_filters["City"] = request.form.get("txtCity")
    if request.form.get("txtMin") != '' and request.form.get("txtMin") is not None:
        my_filters["MinTemp"] = int(request.form.get("txtMin"))
    if request.form.get("txtMax") != '' and request.form.get("txtMax") is not None:
        my_filters["MaxTemp"] = int(request.form.get("txtMax"))
    if request.form.get("txtDate") != '' and request.form.get("txtDate") is not None:
        my_filters["DateRecorded"] = str(request.form.get("txtDate"))
    query = db.session.query(Temps)
    for attr, value in my_filters.items():
        if attr == "MinTemp":
            query = query.filter(getattr(Temps, attr) >= value)
        else:
            if attr == "MaxTemp":
                query = query.filter(getattr(Temps, attr) <= value)
            else:
                query = query.filter(getattr(Temps, attr) == value)
    # count = db.engine.execute('select count(id) from temps').scalar()
    print("Fil: " + str(my_filters))
    records = []
    if m.fullCount != 0:  # this ensures there are results in this filtered set
        mytable = query.all()
        for record in mytable:
            temp_dict = {'id': record.ID, 'city': record.City, 'daterecorded': record.DateRecorded, 'mintemp': record.MinTemp, 'maxtemp': record.MaxTemp}
            # append to records
            records.append(temp_dict)
    else:
        temp_dict = {'id': 0, 'city': '', 'mintemp': 0, 'maxtempt': 0}
        records.append(temp_dict)
    return records


# extract the numeric value from the result
# this splits the string between "(" and ",)", which are in the DB result
def extract_value(in_result):
    m = in_result.split('(', 1)[1].split(',)', 1)[0]
    return m
