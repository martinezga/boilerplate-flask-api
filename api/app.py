import os

from api.configurations import settings
from api.configurations.database import db
from api.routes import register_all_bp
from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_object(settings.ApiConfig())

    if test_config:
        app.config.update(test_config)

    # ensure the instance folder exists
    from contextlib import suppress

    with suppress(OSError):
        os.makedirs(app.instance_path)

    # initialize DB connection
    db.init_app(app)
    # create table schema
    with app.app_context():
        import api.models  # noqa

        db.create_all()
        # Improvement: Implement DB migration

    # register blueprints
    register_all_bp(app)

    return app


if __name__ == "__main__":
    flask_app = create_app()
    flask_app.run()
