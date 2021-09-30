"""
Main file for testing procedures
"""

# import backend.app as app
from datetime import datetime
import pytest
from backend import init_app
from backend.apps.user.utils import create_user

# post = {
#     "title": "titulo1",
#     "description": "descrip", "public": True,
#     "tags": ["1", "2"]
#     }


@pytest.fixture
def client():
    app = init_app(testing=True)
    app.config["TESTING"] = True

    with app.app_context():
        with app.test_client() as client:
            yield client


@pytest.fixture
def user():
    user = create_user(
        username="test_user",
        email="test_user@correo.com",
        first_name="test",
        last_name="test_last",
        ci=23587946,
        password="Aa123456789",
        email_confirmed_at=datetime.utcnow(),
    )


def test_server_status(client):
    rv = client.get("/api/health")
    assert rv.status_code == 200


def test_login(client, user):
    user.save()
    log = client.post('/login', data=dict(
        username=user.username,
        password=user.password
    ))
    assert log.status_code == 200
