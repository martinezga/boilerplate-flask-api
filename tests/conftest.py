import os
import tempfile

import pytest

from api.app import create_app
from api.configurations.database import db


@pytest.fixture(scope="module")
def flask_app():
    db_fd, db_path = tempfile.mkstemp()

    app = create_app()
    app.config.update(
        {
            "TESTING": True,
            "BCRYPT_LOG_ROUNDS": 4,
        }
    )

    with app.app_context():
        db.init_db(app)

    yield app

    # clean up / reset resources here
    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture(scope="module")
def client_test(flask_app):
    """Flask method to make HTTP requests"""
    # Create a test client using the Flask application configured for testing
    # Establish an application context
    with flask_app.test_client() as testing_client, flask_app.app_context():
        yield testing_client  # this is where the testing happens!


# @pytest.fixture(scope='module')
# def init_database():
#     # Create the database and the database table
#     db.create_all()
#
#     # Insert user data
#     user1 = User(email='pat79@gmail.com', plaintext_password='FlaskIs')
#     user2 = User(email='kens@gmail.com', plaintext_password='PaSs')
#     db.session.add(user1)
#     db.session.add(user2)
#
#     # Commit the changes for the users
#     db.session.commit()
#
#     yield db  # this is where the testing happens!
#
#     db.drop_all()
