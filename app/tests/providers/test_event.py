#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from cloudant.client import CouchDB
import mock
from cloudant.client import CouchDB
from injector import inject
from app.providers.couchdb import CouchDBProvider
from app.endpoints.event import EventAPI
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

        # new_event = {
        #     '_id': '6662343827845294592352392345',
        #     'state': 'test',
        #     'operator_id': 'idoperator12345666666666',
        #     'type': 'event'
        # }

    def test_create_event(self):
        print('response')

    def test_get_event(self):
        docTest = {
            '_id': 'julia102',
            'name': 'Julia',
            'age': 30,
            'type': 'event'
        }
        self.db.create_document(docTest)
        provider = CouchDBProvider(self.db)
        doc = provider.get_document('julia102')

        response = self.client.get(
            '/events/{}'.format(
                doc['_id']
            ),
        )

        assert response.status_code == 200