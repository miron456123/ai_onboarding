from curator.app import create_app
from curator.app.db import db
from curator.app.services.catalog import load_courses
from curator.app.services.factory import seed_demo_employees

class TestConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


def test_health_and_seeded_catalog():
    app = create_app(TestConfig)
    client = app.test_client()
    with app.app_context():
        db.create_all()
        load_courses()
        seed_demo_employees()
    assert client.get('/api/health').json == {'status': 'ok'}
    assert len(client.get('/api/courses').json) > 0
    assert len(client.get('/api/employees').json) == 3
