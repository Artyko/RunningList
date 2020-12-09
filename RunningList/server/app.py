from flask import Flask
from flask_cors import CORS
import models
import routes


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'


# register blueprints's
app.register_blueprint(routes.task_routes)


# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


def init_db():
    models.db.init_app(app)
    models.db.app = app
    models.db.create_all()


if __name__ == '__main__':
    init_db()
    app.run()
