from flask import Flask
from flask_migrate import Migrate
from server.config import Config
from server.extensions import db

# Initialize Flask extensions outside the function
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)  # <-- Register Migrate with the app

    from server.models import user, guest, episode, appearance

    return app

app = create_app()
