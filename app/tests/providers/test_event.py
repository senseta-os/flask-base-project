#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from cloudant.client import CouchDB
from app.providers.couchdb import CouchDBProvider
import pytest


@pytest.mark.usefixtures('client_class')
class TestEvent(unittest.TestCase):
    def setUp(self):
        self.client_couchdb = CouchDB(
            user='admin',
            auth_token='SHFJ3QrCBNJAq8pc47LnhxBLsaAfzu',
            url='https://couchbk.stag.sensitve.app',
            connect=True
        )

        self.db = self.client_couchdb.create_database('test')

        self.doc_test = {
            '_id': 'julia102',
            'name': 'Julia',
            'age': 30,
            'type': 'event'
        }
        self.db.create_document(self.doc_test)

        self.event_to_delete = {
            '_id': 'documenttodelete',
            'name': 'Nicolás',
            'age': 15,
            'type': 'event'
        }
        self.db.create_document(self.event_to_delete)

        self.provider = CouchDBProvider(self.client_couchdb, 'test')

    def test_create_event(self):
        event_to_delete = {
            '_id': 'documenttodelete',
            'operator_id': 'Nicolás',
            'state': 'New',
            'doc': 'event'
        }

        response = self.client.post('/events/', data=event_to_delete)

        assert response.status_code == 200
        assert b'event created' in response.data

    def test_get_event(self):
        doc = self.provider.get_document(self.doc_test['_id'])
        response = self.client.get(
            '/events/{}'.format(
                doc['_id']
            ),
        )

        assert response.status_code == 200

    def test_delete_event(self):
        response = self.client.delete(
            '/events/delete/{}'.format(
                self.event_to_delete['_id']
            ),
        )

        assert response.status_code == 200
        assert b'event deleted' in response.data

    def test_error_delete_event(self):
        response = self.client.delete(
            '/events/delete/{}'.format(
                'eventthatdoesnnotexist'
            ),
        )

        assert response.status_code == 200
        assert b'event does not exists' in response.data

    # TODO pending querys
    # def test_get_message(self):
    #     doc = self.provider.get_document(self.doc_test['_id'])

    #     response = self.client.get(
    #         '/events/messages/{}'.format(
    #             doc['_id']
    #         ),
    #     )

    #     assert response.status_code == 200

