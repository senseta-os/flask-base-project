from flask.views import MethodView
from flask import request
from injector import inject
from flask import jsonify

from app.providers.event import EventProvider


class EventAPI(MethodView):

    @inject
    def __init__(self, event: EventProvider):
        self.event = event

    def get(self, event_id):
        event_doc = self.event.get_event(event_id)
        return jsonify(event_doc)

    def post(self):
        doc = self.event.create_event(
            request.form['operator_id'],
            request.form['state'],
        )
        doc_id = doc['_id']
        return f'event created {doc_id}'

    def delete(self, event_id):
        doc = self.event.delete_event(
            self.event.get_event(event_id)
        )
        if doc:
            return f'event deleted {event_id}'
        return f'event does not exists {event_id}'


class EventMessagesAPI(MethodView):

    @inject
    def __init__(self, event: EventProvider):
        self.event = event

    def get(self, event_id):
        messages = self.event.get_messages(event_id)
        return jsonify(messages)
