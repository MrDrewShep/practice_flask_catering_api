from flask import Blueprint, request, redirect, url_for
from services.client_service import client_create, client_login
from flask_jwt_extended import jwt_required, get_jwt_identity

auth_blueprint = Blueprint("auth_api", __name__)

# Login route
    # IN: Email, password
    # OUT: Session token
@auth_blueprint.route('/login', methods=["POST"])
def login():
    data = request.json

    # TODO Check password against stored hash to determine result
    token, message = client_login(data)

    return {
            "message": message,
            "token": token
        }

# Logout route
    # IN: None 
    # OUT: Message
@auth_blueprint.route('/logout', methods=["POST"])
@jwt_required
def logout():

    # TODO deauthenticate the token, see Adam for help

    # MFD
    message = "logged out"

    return {
        "message": message
    }

# Register route
    # IN: Email, password, client name
    # OUT: Message
@auth_blueprint.route('/register', methods=["POST"])
def register():
    data = request.json

    success, message = client_create(data)

    return {
        "success": success,
        "message": message
    }