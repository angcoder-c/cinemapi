from app.models import Ticket, Movie, Function, db
from flask import jsonify
import re

def validate_seat_code(seat: str):
    matched = re.search('^[A-E]\d{1}\d{1}', seat)

    if matched == None:
        return False
    
    letter = matched.group(0)[0]
    number = int(matched.group(0)[1::])

    if number > 0 and number < 11:
        return False
    
    return True

def save_seat(function_id: int, user_id: int, seats: list):
    func = Function.query.filter_by(id=function_id).first()
    errors = []
    status = False
    not_available_message = lambda s: f'seat {s} not available'


    for seat in seats:
        if getattr(func, f'id_{seat}') != None:
            status = False
            errors.append(not_available_message(seat))

        setattr(func, f'id_{seat}', user_id)
        db.session.commit()
        status = True
    return status, errors

def validate_fields(req):
    fields = ['movie_id', 'seating', 'show_id']
    errors = []
    not_sent_message = lambda f: '{field} not sent'.format(field=f)
    invalid_message = lambda f: 'invalid {field}'.format(field=f)

    for field in fields:
        try:
            f = req.json[field]
        except:
            f = ''
            
        if not f:
            errors.append(not_sent_message(field))
        
        if f in ['']:
            errors.append(invalid_message(field))
        
        if type(f) == str:
            if field == 'movie_id' and not Movie.query.filter_by(id=f):
                errors.append(invalid_message(field))
        
            if field == 'show_id' and Function.query.filter_by(id=f).first():
                errors.append(invalid_message(field))
        
        if field == 'seating' and type(f) != list:
            [errors.append(invalid_message(field)) for seat in f if not validate_seat_code(seat)]
    
    if not errors:
        return True, errors
    return False, errors


def create_ticket(req, user_id):
    ticket = Ticket(id_movie=req.json['movie_id'], id_function=req.json['show_id'], id_user=user_id)
    
    db.session.add(ticket)
    db.session.commit()
    return ticket

def get_seating_show_for(show_id, id):
    show = Function.query.filter_by(id=show_id).first()
    
    seats = [
        f'{let}0{i}' if i < 10 else f'{let}{i}'  
        for let in ['A','B','C','D','E'] 
        for i in range(1, 11)
    ]

    useats = []

    for seat in seats:
        value = getattr(show, f'id_{seat}')
        if value == id:
            useats.append(seat)
    return useats

def get_dict_ticket_verbose(id):

    ticket = Ticket.query.filter_by(id=id).first()
    show = Function.query.filter_by(id=ticket.id_function).first()
    movie = Movie.query.filter_by(id=ticket.id_movie).first()

    ret = {
        'id' : ticket.id,
        'seating' : get_seating_show_for(ticket.id_function, ticket.id_user),
        'show' : {
            'id' : show.id,
            'datetime' : show.datetime,
            'movie' : {
                'id' : movie.id,
                'title' : movie.title,
                'poster' : movie.poster,
                'classification' : movie.classification
            }
        }
    }

    return ret

def get_dict_ticket(id):

    ticket = Ticket.query.filter_by(id=id).first()

    ret = {
        'id' : ticket.id,
        'seating' : get_seating_show_for(ticket.id_function, ticket.id_user),
        'show' : ticket.id_function
    }

    return ret

def delete_ticket(id):
    Ticket.query.filter_by(id=id).delete()
    db.session.commit()