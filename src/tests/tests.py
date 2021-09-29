"""
Main file for testing procedures
"""

# import backend.app as app
import pytest
from backend import init_app
from backend.apps.user.models import User
from backend.apps.user.utils import create_user

# post = {
#     "title": "titulo1", 
#     "description": "descrip", "public": True, 
#     "tags": ["1", "2"]
#     }

@pytest.fixture
def user():
    create_user(
        username = "test_user",
        email = "test@correo.com",
        first_name = "test",
        last_name = "test_last",
        ci = 23587946,
    )

@pytest.fixture
def client():
    app = init_app()
    app.config['TESTING'] = True

    with app.app_context():
        with app.test_client() as client:
            yield client

def login(client, user):
    log = client.post('/login', data=dict(
        username=user.username,
        password=user.password
    ), follow_redirects=False)
    assert log.status_code == 200


def test_server_status(client):
    rv = client.get('/api/health')
    assert rv.status_code == 200

def dummy():
    assert True