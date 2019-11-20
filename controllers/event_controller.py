from flask import Blueprint, request, Response
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.event_services import event_create, event_get, event_get_all, event_update, event_delete, is_event_owner, is_event
from . import blacklist

event_blueprint = Blueprint("event_api", __name__)

# Create new event
@event_blueprint.route('/new', methods=["POST"])
@jwt_required
def event_new():
    data = request.json
    message = event_create(data)
    response = {"message": message}
    return response

# Get, Update, Delete a specific event
@event_blueprint.route('/<int:event_id>', methods=["GET", "PUT", "DELETE"])
@jwt_required
def event_specific(event_id):

    print(blacklist)
    client = get_jwt_identity()
    event = is_event(event_id)
    if event:
        if is_event_owner(client, event_id):
            if request.method == "GET":
                response = event_get(event_id)
            elif request.method == "PUT":
                change_data = request.json
                response = event_update(event, change_data)
            elif request.method == "DELETE":
                response = event_delete(event)
        else:
            response = {"message": "Unauthorized to view the selection."}
    else:
        response = {"message": "Invalid event selection."}
    return response

# Get all events belonging to active client
@event_blueprint.route('/all', methods=["GET"])
@jwt_required
def event_all():
    client = get_jwt_identity()
    response = event_get_all(client)
    return response
