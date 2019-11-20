from . import bcrypt
from flask_jwt_extended import create_access_token

def generate_password_hash(password):
    return bcrypt.generate_password_hash(password).decode("utf-8")

# TODO build check password hash

# TODO generate JWT token

# TODO ??? logout or deactivate token?