from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from config import Config
from .models import db, login_manager

migrate = Migrate(compare_type=True)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    jwt = JWTManager(app)

    from .private import private_bp
    app.register_blueprint(private_bp)

    from .public import public_bp
    app.register_blueprint(public_bp)

    return app