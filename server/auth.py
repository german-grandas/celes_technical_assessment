from functools import wraps

from flask import jsonify, request
from firebase_admin import auth


def authenticate_request(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            id_token = request.headers.get("Authorization").replace("Bearer", "")

            if id_token:
                return func(*args, **kwargs)
            else:
                return jsonify({"error": "Unauthorized"}), 403

        except Exception as e:
            return jsonify({"error": str(e)}), 401

    return wrapper
