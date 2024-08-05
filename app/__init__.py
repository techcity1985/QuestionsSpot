from flask import Flask
from .routes.auth import auth
from .routes.main import main
from .models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    app.register_blueprint(auth)
    app.register_blueprint(main)

    return app
