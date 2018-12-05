import unittest
import mock
from cloudant.client import CouchDB
from injector import inject

from app.providers.couchdb import CouchDBProvider


class TestCouchDb(unittest.TestCase):
    def setUp(self):
        self.client_couchdb = CouchDB(
            user='admin',
            auth_token='SHFJ3QrCBNJAq8pc47LnhxBLsaAfzu',
            url='https://couchbk.stag.sensitve.app',
            connect=True
        )
        self.db = self.client_couchdb.create_database('test')

    def test_get_document(self):
        docTest = {
            '_id': 'julia102',
            'name': 'Julia',
            'age': 30,
            'pets': ['cat', 'dog', 'frog']
        }
        self.db.create_document(docTest)
        # act
        provider = CouchDBProvider(self.client_couchdb, 'test')
        doc = provider.get_document('julia102')

        assert doc['_id'] == docTest['_id']

    def test_document_not_exist(self):
        provider = CouchDBProvider(self.client_couchdb, 'test')
        doc = provider.get_document('julianoexists')

        assert doc is None