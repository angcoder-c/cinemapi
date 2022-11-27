from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from sqlalchemy.types import Text
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'public_bp.login'

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    firstname = db.Column(db.String(128), nullable = False)
    lastname = db.Column(db.String(128), nullable = False)
    username = db.Column(db.String(64), nullable = False, unique = True)
    password = db.Column(db.String(256), nullable = False)
    email = db.Column(db.String(128), nullable = False, unique = True)
    phone = db.Column(db.Unicode(255))
    phone_country_code = db.Column(db.Unicode(8))
    tickets = db.relationship('Ticket', backref='user_tickets', lazy='dynamic')
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __init__(
                 self, firstname, lastname, 
                 username, password, email, 
                 phone, phone_country_code
                 ):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password
        self.email = email
        self.phone = phone
        self.phone_country_code = phone_country_code

    def __str__(self):
        return f'User {self.id}'

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    title = db.Column(db.String(256), nullable = False, unique = True)
    poster = db.Column(Text(), nullable = False)
    trailer = db.Column(Text(), nullable = False)
    classification = db.Column(db.String(8), nullable = False)
    functions = db.relationship('Function', backref='function', lazy='dynamic')
    tickets = db.relationship('Ticket', backref='tickets', lazy='dynamic')
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __str__(self):
        return f'Movie {self.id}'

    def __init__(
                 self, title, poster, 
                 trailer, classification
                 ):
        self.title = title
        self.poster = poster
        self.trailer = trailer
        self.classification = classification

class Function(db.Model):

    __tablename__ = 'functions'

    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    id_movie = db.Column(db.Integer, db.ForeignKey('movies.id'))
    tickets = db.relationship('Ticket', backref='movie_tickets', lazy='dynamic')
    datetime = db.Column(db.DateTime(timezone=True))
    code = db.Column(db.String(4), nullable=False)
    theater_number = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    id_A01 = db.Column(db.Integer, nullable=True)
    id_A02 = db.Column(db.Integer, nullable=True)
    id_A03 = db.Column(db.Integer, nullable=True)
    id_A04 = db.Column(db.Integer, nullable=True)
    id_A05 = db.Column(db.Integer, nullable=True)
    id_A06 = db.Column(db.Integer, nullable=True)
    id_A07 = db.Column(db.Integer, nullable=True)
    id_A08 = db.Column(db.Integer, nullable=True)
    id_A09 = db.Column(db.Integer, nullable=True)
    id_A10 = db.Column(db.Integer, nullable=True)

    id_B01 = db.Column(db.Integer, nullable=True)
    id_B02 = db.Column(db.Integer, nullable=True)
    id_B03 = db.Column(db.Integer, nullable=True)
    id_B04 = db.Column(db.Integer, nullable=True)
    id_B05 = db.Column(db.Integer, nullable=True)
    id_B06 = db.Column(db.Integer, nullable=True)
    id_B07 = db.Column(db.Integer, nullable=True)
    id_B08 = db.Column(db.Integer, nullable=True)
    id_B09 = db.Column(db.Integer, nullable=True)
    id_B10 = db.Column(db.Integer, nullable=True)

    id_C01 = db.Column(db.Integer, nullable=True)
    id_C02 = db.Column(db.Integer, nullable=True)
    id_C03 = db.Column(db.Integer, nullable=True)
    id_C04 = db.Column(db.Integer, nullable=True)
    id_C05 = db.Column(db.Integer, nullable=True)
    id_C06 = db.Column(db.Integer, nullable=True)
    id_C07 = db.Column(db.Integer, nullable=True)
    id_C08 = db.Column(db.Integer, nullable=True)
    id_C09 = db.Column(db.Integer, nullable=True)
    id_C10 = db.Column(db.Integer, nullable=True)

    id_D01 = db.Column(db.Integer, nullable=True)
    id_D02 = db.Column(db.Integer, nullable=True)
    id_D03 = db.Column(db.Integer, nullable=True)
    id_D04 = db.Column(db.Integer, nullable=True)
    id_D05 = db.Column(db.Integer, nullable=True)
    id_D06 = db.Column(db.Integer, nullable=True)
    id_D07 = db.Column(db.Integer, nullable=True)
    id_D08 = db.Column(db.Integer, nullable=True)
    id_D09 = db.Column(db.Integer, nullable=True)
    id_D10 = db.Column(db.Integer, nullable=True)

    id_E01 = db.Column(db.Integer, nullable=True)
    id_E02 = db.Column(db.Integer, nullable=True)
    id_E03 = db.Column(db.Integer, nullable=True)
    id_E04 = db.Column(db.Integer, nullable=True)
    id_E05 = db.Column(db.Integer, nullable=True)
    id_E06 = db.Column(db.Integer, nullable=True)
    id_E07 = db.Column(db.Integer, nullable=True)
    id_E08 = db.Column(db.Integer, nullable=True)
    id_E09 = db.Column(db.Integer, nullable=True)
    id_E10 = db.Column(db.Integer, nullable=True)

    def __init__(
                 self, id_movie, datetime, 
                 code, theater_number
                 ):
        self.id_movie = id_movie
        self.datetime = datetime
        self.code = code
        self.theater_number = theater_number
    
    def __str__(self):
        return f'Function {self.id}'

class Ticket(db.Model):
    
    __tablename__ = 'tickets'

    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    id_movie = db.Column(db.Integer, db.ForeignKey('movies.id'), nullable=False)
    id_function = db.Column(db.Integer, db.ForeignKey('functions.id'), nullable=False)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __init__(
                 self, id_movie, id_function, 
                 id_user
                 ):
        self.id_movie = id_movie
        self.id_function = id_function
        self.id_user = id_user
    
    def __str__(self):
        return f'Ticket {self.id}'
    
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))