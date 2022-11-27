from app.models import User

def get_dict_user(id):
    u = User.query.filter_by(id=id).first()

    if not (u != None):
        user = {'message' : 'user not found'}
        return user

    user = {
        'firstname' : u.firstname, 
        'lastname' : u.lastname, 
        'username' : u.username, 
        'password' : u.password, 
        'email' : u.email, 
        'phone' : u.phone, 
        'phone_country_code' : u.phone_country_code
    }

    return user