from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from server.config import Config

#initialize Flask extensions
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

#application factory function
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    #initialize extensions with the app
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    return app
