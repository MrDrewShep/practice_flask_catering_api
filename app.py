from flask import Flask
from controllers import auth_blueprint, event_blueprint
from models import db#, Client, Event    # Client, Event for db setup only
from services import bcrypt, jwt

app = Flask(__name__)


# Setting our configuration file
app.config.from_object("config.Development")
db.init_app(app)
bcrypt.init_app(app)
jwt.init_app(app)

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