from app.models import User
from flask_jwt_extended import create_access_token
import re

def validate_register_data(req):
    fields = ['firstname', 'lastname', 'username', 'password', 'email', 'phone', 'phone_country_code']
    errors = []
    not_sent_message = lambda f: '{field} not sent'.format(field=f)
    invalid_message = lambda f: 'invalid {field}'.format(field=f)
    already_exist_message = lambda f: '{field} already exist'.format(field=f)

    for field in fields:
        try:
            f = req.json[field]
        except:
            f = ''

        if not f:
            errors.append(not_sent_message(field))
        
        if f in ['']:
            errors.append(invalid_message(field))

        if field == 'phone' and not (re.search("(\d{4}){2}", f) != None):
            errors.append(invalid_message(field))
        
        if field == 'username' and User.query.filter_by(username=f).first():
            errors.append(already_exist_message(field))
        
        if field == 'email' and User.query.filter_by(email=f).first():
            errors.append(already_exist_message(f))
    
    if not errors:
        return True, errors
    return False, errors

def validate_login_data(req):
    fields = ['email', 'password']
    errors = []
    not_sent_message = lambda f: '{field} not sent'.format(field=f)
    invalid_message = lambda f: 'invalid {field}'.format(field=f)
    not_found_message = 'user not found'
    bad_password_message = 'user found, wrong password'

    for field in fields:
        try:
            f = req.json[field]
        except:
            f = ''

        if not f:
            errors.append(not_sent_message(field))
        
        if f in ['']:
            errors.append(invalid_message(field))
        
        if field == 'email' and not User.query.filter_by(email=f).first():
            errors.append(not_found_message)
        
        if field == 'password' and not User.query.filter_by(password=f).first():
            errors.append(bad_password_message)
    
    if not errors:
        return True, errors
    return False, errors

def create_user(req):
    user = {
        'firstname' : req.json['firstname'], 
        'lastname' : req.json['lastname'], 
        'username' : req.json['username'], 
        'password' : req.json['password'], 
        'email' : req.json['email'], 
        'phone' : req.json['phone'], 
        'phone_country_code' : req.json['phone_country_code']
    }

    return User(**user)


def create_token(email, password):
    user = User.query.filter_by(email=email, password=password).first()

    if user == None:
        return {
            'status' : 'error',
            "message": "bad email or password"
        }
    
    token = create_access_token(identity=user.id)
    return {
        'status' : 'success',
        'message' : 'user logged in successfully',
        'token': token}