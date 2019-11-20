from datetime import datetime
from . import db

from marshmallow import Schema, fields

class Event(db.Model):
    __tablename__ = "events"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    menu_choice = db.Column(db.Integer)
    event_date = db.Column(db.DateTime)
    client_id = db.Column(db.Integer, db.ForeignKey("clients.id"))
    created_at = db.Column(db.DateTime)
    last_modified = db.Column(db.DateTime)

    data = {
        "title": title,
        "menu_choice": menu_choice,
        "event_date": event_date,
        "client_id": client_id
    }

    def __init__(self, data):
        self.title = data["title"]
        self.menu_choice = data["menu_choice"]
        self.event_date = data["event_date"]
        self.client_id = data["client_id"]
        now = datetime.utcnow()
        self.created_at = now
        self.last_modified = now

    def save(self):
        db.session.add(self)
        db.session.commit()
        return f'Blog post successfully created "{self.title}"'

    def update(self, event, change_data):
        for key, item in change_data.items():
            setattr(event, key, item)
        self.last_modified = datetime.utcnow()
        db.session.commit()
        return event

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def event_get(event_id):
        return Event.query.filter_by(id=event_id).first()

    @staticmethod
    def event_get_all(client):
        events = Event.query.filter_by(client_id=client)
        return events

    @staticmethod
    def event_get_owner(event_id):
        return Event.query.filter_by(id=event_id).first().client_id

class EventSchema(Schema):
    id = fields.Int(dump_only=True)
    client_id = fields.Int(required=True, dump_only=True)
    title = fields.Str(dump_only=True)
    menu_choice = fields.Str(dump_only=True)
    event_date = fields.DateTime(dump_only=True)