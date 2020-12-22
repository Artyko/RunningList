from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import Config
from flask_cors import CORS


db = SQLAlchemy()
ma = Marshmallow()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    ma.init_app(app)

    from app.routes import task_routes
    app.register_blueprint(task_routes)

    CORS(app, resources={r'/*': {'origins': '*'}})

    return app


from app import models
