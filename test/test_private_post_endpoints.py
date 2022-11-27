from . import test_app_post_private
import json

def test_my_tickets_user():
    response_login = test_app_post_private.post("/login/", content_type='application/json', data=json.dumps({
        'password' : '123', 
        'email' : 'michael@email.com'
    }))

    test_app_post_private.environ_base['HTTP_AUTHORIZATION'] = 'Bearer ' + response_login.json['token']
    response = test_app_post_private.post("/tickets/buy/", content_type='application/json', data=json.dumps({
        'movie_id' : 1, 
        'seating' : ['A03', 'B03'], 
        'show_id' : 1
    }))

    status = response.json['status']
    message = response.json['message']

    assert status == 'success'
    assert message == 'Ticket created successfully'
    assert response.status_code == 200