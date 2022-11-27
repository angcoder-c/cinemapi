from . import test_app_post_public
import json
from faker import Faker
 
fake = Faker()


def test_register_user():
    profile = fake.simple_profile()
    response = test_app_post_public.post("/signin/", content_type='application/json', data=json.dumps({
        'firstname' : profile['name'].split(' ')[0], 
        'lastname' : profile['name'].split(' ')[1], 
        'username' : profile['username'], 
        'password' : '123', 
        'email' : profile['mail'],
        'phone' : '12345678', 
        'phone_country_code' : '502'
    }))

    assert response.json['message'] == 'User created successfully'
    assert response.json['status'] == 'success'
    assert response.status_code == 200

def test_login_user():
    response = test_app_post_public.post("/login/", content_type='application/json', data=json.dumps({
        'password' : '123', 
        'email' : 'ryan@email.com'
    }))

    assert response.json['message'] == 'user logged in successfully'
    assert response.json['status'] == 'success'
    assert type(response.json['token']) == str
    assert response.status_code == 200

def test_logout_endpoint():    
    response = test_app_post_public.get('/logout/')

    assert response.json['status'] == 'success'
    assert response.json['messages'] == 'session successfully closed'