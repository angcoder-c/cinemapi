from . import test_app_get_public

def test_index_endpoint():    
    response = test_app_get_public.get('/')
    assert response.status_code == 302

def test_invalid_route():    
    response = test_app_get_public.get('/invalid/')

    assert response.json['status'] == 'error'
    assert response.json['message'] == 'this route does not exist'
    assert response.status_code == 200

def test_movie_endpoint():    
    response = test_app_get_public.get('/movies/')

    movies = response.json['movies']
    movie = movies[0]
    id = movie['id']
    title = movie['title']
    poster = movie['poster']
    classification = movie['classification']
    shows = movie['shows']
    show = shows[0]
    id_show = show['id']
    datetime_show = show['datetime']

    assert type(movies) == list
    assert type(movie) == dict
    assert type(id) == int
    assert type(title) == str
    assert type(poster) == str
    assert type(classification) == str
    assert type(shows) == list
    assert type(show) == dict
    assert type(id_show) == int
    assert type(datetime_show) == str
    assert response.status_code == 200


def test_tickets_endpoint():    
    response = test_app_get_public.get('/tickets/')

    tickets = response.json['tickets']
    ticket = tickets[0]
    id = ticket['id']
    seating = ticket['seating']
    seat = ticket['seating'][0]
    show = ticket['show']
    show_id = show['id']
    show_datetime = show['datetime']
    movie = show['movie']
    movie_id = movie['id']
    movie_classification = movie['classification']
    movie_poster = movie['poster']
    movie_title = movie['title']

    assert type(tickets) == list
    assert type(ticket) == dict
    assert type(id) == int
    assert type(seating) == list
    assert type(seat) == str
    assert type(show) == dict
    assert type(show_id) == int
    assert type(show_datetime) == str
    assert type(movie) == dict
    assert type(movie_id) == int
    assert type(movie_classification) == str
    assert type(movie_poster) == str
    assert type(movie_title) == str
    assert response.status_code == 200

def test_shows_endpoint():    
    response = test_app_get_public.get('/shows/')

    shows = response.json['shows']
    show = shows[0]
    show_key = list(show.keys())[0]
    show_value = list(show.values())[0]
    id = show_value['id']
    datetime = show_value['datetime']
    movie = show_value['movie']
    id_movie = movie['id']
    poster_movie = movie['poster']
    title_movie = movie['title']

    assert type(shows) == list
    assert type(show) == dict
    assert show_key == 'show'
    assert type(show_value) == dict
    assert type(id) == int
    assert type(datetime) == str
    assert type(movie) == dict
    assert type(id_movie) == int
    assert type(poster_movie) == str
    assert type(title_movie) == str
    assert response.status_code == 200
