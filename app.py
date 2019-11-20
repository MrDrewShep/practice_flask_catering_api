from flask import Flask
from controllers import auth_blueprint, event_blueprint, blacklist
from models import db#, Client, Event    # Client, Event for db setup only
from services import bcrypt, jwt

app = Flask(__name__)


# Setting our configuration file
app.config.from_object("config.Development")
db.init_app(app)
bcrypt.init_app(app)
jwt.init_app(app)

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypyted_token):
    jti = decrypyted_token["jti"]
    return jti in blacklist

# Add blueprints here
app.register_blueprint(auth_blueprint, url_prefix="/auth")
app.register_blueprint(event_blueprint, url_prefix="/event")

# MFD
@app.route('/', methods=["GET"])
def basic():
    return {
        "message": "You hit the root endpoint"
    }

if __name__ == "__main__":
    app.run()