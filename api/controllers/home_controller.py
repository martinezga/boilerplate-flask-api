from flask import make_response


def home():
    message = {
        "description": "Basic Flask API REST",
        "detail": "Up and running",
        "status_code": 200,
    }

    response = make_response(message, message.get("status_code"))

    return response
