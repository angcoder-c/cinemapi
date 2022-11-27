from . import private_bp
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from app.func_utils.auth import create_token
from flask_login import current_user, logout_user, login_required
from flask import jsonify, request
from app.models import User, Ticket, Function
from app.func_utils.tickets import validate_seat_code, create_ticket, save_seat, get_dict_ticket, get_dict_ticket_verbose, delete_ticket, validate_fields
import datetime

@private_bp.route('/tickets/my/', methods=['GET'])
@jwt_required()
def my_tickets():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)

    tickets = Ticket.query.filter_by(id_user=user.id).all()

    if not tickets:
        return jsonify({
            'status' : 'error',
            'message' : 'no purchased tickets found'
        })

    return jsonify({
        'status' : 'success',
        'message' : 'ticket successfully found',
        'tickets' : [
            get_dict_ticket_verbose(ticket.id)
            for ticket in tickets
        ]
    })


@private_bp.route('/tickets/buy/', methods=['POST'])
@jwt_required()
def buy_ticket():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)

    val_fields = validate_fields(req=request)
    if not val_fields[0]:
        return {
            'status': 'error',
            'messages' : val_fields[1]
        }

    seating = save_seat(
        function_id=request.json['show_id'], 
        user_id=user.id, 
        seats=request.json['seating']
    )

    if not seating[0]:
        return {
            'status': 'error',
            'messages' : seating[1]
        }
    ticket = create_ticket(req=request, user_id=user.id)
    return jsonify({
            'status' : 'success',
            'message' : 'Ticket created successfully',
            'ticket' : get_dict_ticket(ticket.id)
    })

@private_bp.route('/tickets/cancel/', methods=['POST'])
@jwt_required()
def cancel_ticket():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    ret = {
        'status' : 'error',
        'message' : 'the show related to this ticket has already expired'
    }
    try:
        id = request.json['ticket_id']
    except:
        id = 0

    ticket = Ticket.query.filter_by(id_user=user.id, id=id).first()
    if ticket == None:
        return {
            'status' : 'error',
            'message' : 'ticket not found'
        }
    show = Function.query.filter_by(id=ticket.id_function).first()
    if show.datetime > datetime.datetime.now():
        delete_ticket(ticket.id)

        ret['status'] = 'success'
        ret['message'] = 'ticket deleted successfully'
    return jsonify(ret)