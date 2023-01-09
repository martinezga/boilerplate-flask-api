from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = ""  # without trailing '/'
API_URL = "/static/swagger.json"

# Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={"app_name": "Flask API REST"},  # Swagger UI config overrides
    # OAuth config.
    # See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
    # oauth_config={
    #    'clientId': "your-client-id",
    #    'clientSecret': "your-client-secret-if-required",
    #    'realm': "your-realms",
    #    'appName': "your-app-name",
    #    'scopeSeparator': " ",
    #    'additionalQueryStringParams': {'test': "hello"}
    # }
)
