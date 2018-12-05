from injector import inject

from app.providers.couchdb import CouchDBProvider


class UserCouchDBProvider(object):

    @inject
    def __init__(self, database: CouchDBProvider):
        self.db = database.db

    def create_user(self, name, phone, email, birth):
        data = {
            'name': name,
            'phone': phone,
            'email': email,
            'birth': birth
        }

        return self.db.create_document(data)