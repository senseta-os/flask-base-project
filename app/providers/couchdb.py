from cloudant.client import CouchDB
from datetime import datetime
from random import random
from injector import inject


class CouchDBProvider(object):

    @inject
    def __init__(self, db_client: CouchDB, db_name):
        self.db_client = db_client
        self.db = self.db_client[db_name]

    def get_document(self, doc_id):
        if doc_id not in self.db:
            return None
        doc = self.db[doc_id]
        doc.fetch()
        return doc

    def generator_id(self):
        datetime_ = datetime.now()
        str_new_datetime = datetime_.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        return f'{str_new_datetime}_{random()}'

    def create_document(self, doc):
        return self.db.create_document(doc)

    def delete_document(self, doc):
        if doc:
            return doc.delete()
        return False

    def exec_view(self, path, params={}):
        view_path = '{}/{}/_design/{}'.format(
            self.db_client.server_url,
            self.db_name,
            path
        )

        response = self.db_client.r_session.get(view_path, params=params)
        json_response = response.json()

        if response.status_code != 200:
            raise Exception(
                f'Something went wrong while executing a view \n{view_path}'
            )
        else:
            return json_response['rows']
