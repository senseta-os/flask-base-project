from injector import inject

from app.providers.couchdb import CouchDBProvider


class EventProvider(object):

    @inject
    def __init__(self, couchdb: CouchDBProvider):
        self.couchdb = couchdb

    def get_event(self, event_id):
        return self.couchdb.get_document(doc_id=event_id)

    def create_event(
        self,
        operator_id,
        state,
    ):
        new_event = {
            '_id': self.couchdb.generator_id(),
            'state': state,
            'operator_id': operator_id,
            'type': 'event'
        }
        return self.couchdb.create_document(new_event)

    def delete_event(self, event_id):
        return self.couchdb.delete_document(event_id)

    def get_messages(self, event_id):
        params = {
            'include_docs': True,
            'keys': f'["{event_id}"]'
        }
        view_path = 'messages/_view/by_event'
        messages = self.couchdb.exec_view(view_path, params)

        messages_docs = []
        for message in messages:
            messages_docs.append(message['doc'])
        return messages_docs
