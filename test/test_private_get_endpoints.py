from . import test_app_get_private
import json

def test_my_tickets_user():
    response_login = test_app_get_private.post("/login/", content_type='application/json', data=json.dumps({
        'password' : '123', 
        'email' : 'michael@email.com'
    }))

    test_app_get_private.environ_base['HTTP_AUTHORIZATION'] = 'Bearer ' + response_login.json['token']
    response = test_app_get_private.get("/tickets/my/")

    ticket = response.json['tickets'][0]
    id = ticket['id']
    seating = ticket['seating'][0]
    show = ticket['show']
    datetime = show['datetime']
    show_id = show['id']
    movie = show['movie']
    classification_movie = movie['classification']
    id_movie = movie['id']
    poster_movie = movie['poster']
    title_movie = movie['title']

    assert response.json['message'] == 'ticket successfully found'
    assert response.json['status'] == 'success'
    assert type(response.json['tickets']) == list
    assert type(ticket) == dict
    assert type(id) == int
    assert type(seating) == str
    assert type(show) == dict
    assert type(datetime) == str
    assert type(show_id) == int
    assert type(movie) == dict
    assert type(classification_movie) == str
    assert type(id_movie) == int
    assert type(poster_movie) == str
    assert type(title_movie) == str
    assert response.status_code == 200
