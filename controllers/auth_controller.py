from flask import Blueprint, request, redirect, url_for, jsonify

from . import blacklist
from services.client_service import client_create, client_login
from flask_jwt_extended import jwt_required, get_jwt_identity, get_raw_jwt

auth_blueprint = Blueprint("auth_api", __name__)

# Login route
@auth_blueprint.route('/login', methods=["POST"])
def login():
    data = request.json

    token, message = client_login(data)

    return {
            "message": message,
            "token": token
        }

# Logout route
@auth_blueprint.route('/logout', methods=["DELETE"])
@jwt_required
def logout():
    jti = get_raw_jwt()["jti"]
    blacklist.add(jti)
    return jsonify({"message": "Successfully logged out."}), 200

# Register route
@auth_blueprint.route('/register', methods=["POST"])
def register():
    data = request.json

    success, message = client_create(data)

    return {
        "success": success,
        "message": message
    }