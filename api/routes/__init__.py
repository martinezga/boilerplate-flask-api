from .home_bp import home_bp


def register_all_bp(flask_app):

    flask_app.register_blueprint(home_bp)
