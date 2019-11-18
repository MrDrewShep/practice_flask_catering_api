from flask import Blueprint, request

auth_blueprint = Blueprint("auth_api", __name__)

# Login route
# IN: Email, password
# OUT: Session token
@auth_blueprint.route('/login', methods=["POST"])
def login():
    data = request.json

    # TODO Check password against stored hash to determine result

    return {
        "message": "logged in",
        "email": data["email"],
        "password": data["password"]
    }

# Logout route
# IN: None 
# OUT: Message
@auth_blueprint.route('/logout', methods=["POST"])
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

    # TODO create a user

    # MFD
    message = "user created successfully"

    return {
        "message": message
    }