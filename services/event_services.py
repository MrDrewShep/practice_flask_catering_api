from flask import Response, json
from models.event_model import Event, EventSchema
from flask_jwt_extended import get_jwt_identity

event_schema = EventSchema()

def is_event_owner(client, event_id):
    return True if client == Event.event_get_owner(event_id) else False

def is_event(event_id):
    return Event.event_get(event_id)

def event_create(data):
    if data["menu_choice"] in [1, 2, 3]:
        data["client_id"] = get_jwt_identity()
        new_event = Event(data)
        try:
            new_event.save()
            message = f'New event successfully created: {data["title"]}'
            return message, 200
        except Exception as e:
            return str(e), 400
    else:
        message = "Select a menu choice 1-3."
    return message

def event_get(event_id):
    event = is_event(event_id)
    schema_dump = event_schema.dump(event)
    response = custom_response(schema_dump, 200)
    return response

def event_get_all(client):
    events = Event.event_get_all(client)
    schema_dump = event_schema.dump(events, many=True)
    response = custom_response(schema_dump, 200)
    return response

def event_update(event, change_data):
    event.update(event, change_data)
    schema_dump = event_schema.dump(event)
    response = custom_response(schema_dump, 200)
    return response

def event_delete(event):
    event.delete()
    response = {"message": f'{event.title} deleted successfully.'}
    return response

def custom_response(response, status_code):
    return Response(
        mimetype='application/json',
        response=json.dumps(response),
        status=status_code
    )