from app import create_app, db
from config import Config

app = create_app()


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


class TestUserModelCase:
    def setup(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def teardown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()


class TestAPI:
    def setup(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_get_api_endpoint(self):
        r = self.app.get('/tasks')
        print(r.json["status"])
        assert r.json["status"] == "success"
        assert r.status_code == 200
