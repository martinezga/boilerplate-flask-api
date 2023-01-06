from flask import Flask

from api.configurations import settings
from api.configurations.database import db
from api.routes import register_all_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(settings.ApiConfig())

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
    app = create_app()
    app.run(
        host=app.config.get("DB_SERVER"),
        port=app.config.get("PORT"),
        debug=app.config.get("DEBUG"),
    )
