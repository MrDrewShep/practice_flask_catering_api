from flask import Flask
from controllers import auth_blueprint, event_blueprint

app = Flask(__name__)

# Add blueprints here
app.register_blueprint(auth_blueprint, url_prefix="/auth")
app.register_blueprint(event_blueprint, url_prefix="/event")

# MFD
@app.route('/', methods=["GET"])
def basic():
    return {
        "message": "Sup, Drew?"
    }

if __name__ == "__main__":
    app.run()