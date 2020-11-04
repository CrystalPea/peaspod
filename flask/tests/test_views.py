import os
import tempfile

import pytest

from flask import url_for
from app import app
from app.views import homepage


@pytest.fixture
def client():
    db_fd, app.app.config['DATABASE'] = tempfile.mkstemp()
    app.app.config['TESTING'] = True

    with app.app.test_client() as client:
        with app.app.app_context():
            app.init_db()
        yield client

    os.close(db_fd)
    os.unlink(app.app.config['DATABASE'])


def test_homepage_loads_correctly(client):
    response = client.get(url_for(homepage))
    assert "Welcome to Pea's Pod" in response.data
