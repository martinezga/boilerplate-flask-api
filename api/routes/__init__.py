from routes.swagger_bp import swaggerui_blueprint

from api.routes.home_bp import home_bp


def register_all_bp(flask_app):

    flask_app.register_blueprint(home_bp)
    flask_app.register_blueprint(swaggerui_blueprint)
