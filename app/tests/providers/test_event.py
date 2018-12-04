#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import mock
from app.providers.couchdb import CouchDBProvider
from cloudant.client import CouchDB


def test_get_document(client):
    # arrange
    client_couchdb = CouchDB(
        user='admin',
        auth_token='SHFJ3QrCBNJAq8pc47LnhxBLsaAfzu',
        url='https://couchbk.stag.sensitve.app',
        connect=True
    )
    db = client_couchdb.create_database('test')
    docTest = {
        '_id': 'julia30',
        'name': 'Julia',
        'age': 30,
        'pets': ['cat', 'dog', 'frog']
    }
    db.create_document(docTest)
    # act
    provider = CouchDBProvider(client_couchdb)
    doc = provider.get_document('julia30')
    # assert
    assert doc['_id'] == docTest['_id']