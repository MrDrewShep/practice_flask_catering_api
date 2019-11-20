from datetime import datetime
from . import db

class Client(db.Model):
    __tablename__ = "clients"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(500), nullable=False)
    name = db.Column(db.String(30), nullable=False)
    created_at = db.Column(db.DateTime)
    last_modified = db.Column(db.DateTime)

    data = {
        "email": email,
        "password": password,
        "name": name,
    }

    def __init__(self, data):
        self.email = data["email"]
        self.password = data["password"]
        self.name = data["name"]
        now = datetime.utcnow()
        self.created_at = now
        self.last_modified = now

    def save(self):
        db.session.add(self)
        db.session.commit()
        return f'Client {self.name} successfully created.'

    @staticmethod
    def check_if_user_exists(email):
        return Client.query.filter_by(email=email).first()

    @staticmethod
    def grab_client(email):
        return Client.query.filter_by(email=email).first()