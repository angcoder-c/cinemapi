from . import public_bp
from app.func_utils.movies import get_all_movie_endpoint
from app.func_utils.auth import validate_register_data, validate_login_data, create_user, create_token
from app.func_utils.tickets import get_dict_ticket_verbose
from app.func_utils.users import get_dict_user
from app.func_utils.shows import get_dict_show_verbose
from app.models import db, User, Ticket, Function
from flask import jsonify, request, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required

@public_bp.route('/', methods=['GET'])
def index():
    return redirect(url_for('public_bp.movies'))

@public_bp.route('/movies/', methods=['GET'])
def movies():
    return jsonify(get_all_movie_endpoint())

@public_bp.route('/signin/', methods=['POST'])
def signin():
    if current_user.is_authenticated:
        return jsonify({
            'status' : 'error',
            'message' : 'this user is already registered'
        })

    if validate_register_data(req=request)[0]:
        user = create_user(request)
        
        db.session.add(user)
        db.session.commit()

        return jsonify({
            'status' : 'success',
            'message' : 'User created successfully',
            'user' : get_dict_user(user.id)
        })

    return {
        'status': 'error',
        'messages' : validate_register_data(req=request)[1]
    }

@public_bp.route('/login/', methods=['POST'])
def login():
    if current_user.is_authenticated:
        return jsonify({
            'status' : 'error',
            'message' : 'this user is already logged in'
        })
    print(request.json['email'], request.json['password'])

    if validate_login_data(req=request)[0]:
        token = create_token(request.json['email'], request.json['password'])
        login_user(User.query.filter_by(email=request.json['email']).first(), remember=True)
        return jsonify(token)

    return {
        'status': 'error',
        'messages' : validate_login_data(req=request)[1]
    }

@public_bp.route('/logout/', methods=['GET'])
def logout():
    if not current_user.is_authenticated:
        return jsonify({
            'status' : 'error',
            'message' : 'unlogged user'
        })

    logout_user()
    return {
        'status': 'success',
        'messages' : 'session successfully closed'
    }

@public_bp.route('/tickets/', methods=['GET'])
def tickets():

    return {
        'tickets' : 
        [get_dict_ticket_verbose(t.id) for t in Ticket.query.all()]
    }

@public_bp.route('/shows/', methods=['GET'])
def shows():

    return {
        'shows' : 
        [get_dict_show_verbose(f.id) for f in Function.query.all()]
    }