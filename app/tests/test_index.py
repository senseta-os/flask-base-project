import unittest
import tempfile
import os.path
from unittest.mock import MagicMock
from app.providers.event import EventProvider
from app.providers.couchdb import CouchDBProvider


def test_index(client):
    response = client.get('/')

    assert b'Hello from Flask' in response.data
    assert b'Hola' not in response.data


def test_create_event(client):
    new_event = {
        'state': 'test',
        'operator_id': 'idoperator12345666666666',
        'type': 'event'
    }
    response = client.post('/events/', data=new_event)

    # self.couchdb.create_document(new_event)

    print(response)
    print(response.data)
    assert response.status_code == 200
    assert b'event created' in response.data


def test_delete_event(client):
    mock = EventProvider(couchdb=CouchDBProvider)
    mock.delete_event = MagicMock(name='delete_event')
    mock.delete_event(
        doc='2018-11-30T21:27:14.026401Z_0.9461661960476352'
    )

    mock.delete_event.assert_called_with(
        doc='2018-11-30T21:27:14.026401Z_0.9461661960476352'
    )


def test_messages(client):
    response = client.get('/')

    assert b'Hello from Flask' in response.data
    assert b'Hola' not in response.data