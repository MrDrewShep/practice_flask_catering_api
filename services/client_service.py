
from models.client_model import Client
from .auth_service import generate_password_hash, create_access_token
from services import bcrypt

def client_create(data):
    # 1 Check if client exists in db
    if not Client.is_client(data["email"]):
        # 2 Hash the password
        data["password"] = generate_password_hash(data["password"])
        # 3 Create the client object
        new_client = Client(data)
        # 4 Save to the db
        message = new_client.save()
        success = True
    else:
        success = False
        message = "Email already registered."

    return success, message

def client_login(data):
    message = "Login failure."
    my_client = Client.is_client(data["email"])
    token = None
    if my_client:
        if bcrypt.check_password_hash(my_client.password, data["password"]):
            token = create_access_token(identity=my_client.id)
            message = "Successfully logged in."
    return token, message
