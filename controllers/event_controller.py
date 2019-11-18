from flask import Blueprint, request

event_blueprint = Blueprint("event_api", __name__)

# New event route
# IN: Event title, menu choice, date
# OUT: Message
@event_blueprint.route('/new', methods=["POST"])
def event_new():
    data = request.json

    # TODO Parse data information and create a new event record

    # MFD
    message = "New event created"

    return {
        "message": message
    }

# Specific event route: GET, PUT, DELETE
# GET
# IN: Event ID
# OUT: The event data
# PUT
# IN: The event data, and event ID
# OUT: Message
# DELETE
# IN: Event ID
# OUT: Message
@event_blueprint.route('/<int:event_id>', methods=["GET", "PUT", "DELETE"])
def event_specific(event_id):
    if request.method == "GET":
        pass
        # TODO build logic

    elif request.method == "PUT":
        pass
        # TODO build logic

    elif request.method == "DELETE":
        pass
        # TODO build logic


    # MFD
    response_dict = {
        "message": "event 1 changed"
    }


    return response_dict

# All events route
# IN: None
# OUT: A dict of all events
@event_blueprint.route('/all', methods=["GET"])
def event_all():
    #TODO build logic

    # MFD
    response_dict = {
        "event 1": "event 1 deets",
        "event 2": "event 2 deets"
    }

    return response_dict