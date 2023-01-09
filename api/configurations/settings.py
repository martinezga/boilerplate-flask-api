from decouple import config


class ApiConfig:
    ENV = config("ENV", default="development")
    DB_SERVER = config("DB_SERVER", default="localhost")
    PORT = config("PORT", default=8000, cast=int)
    DEBUG = config("DEBUG", default=False, cast=bool)
    SQLALCHEMY_DATABASE_URI = config("SQLALCHEMY_DATABASE_URI", default="")
    # Turn off the Flask-SQLAlchemy event system and warning
    SQLALCHEMY_TRACK_MODIFICATIONS = config(
        "SQLALCHEMY_TRACK_MODIFICATIONS",
        default=False,
        cast=bool,
    )
