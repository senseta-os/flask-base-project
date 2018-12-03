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

# def test_get_event(client):
#     response = client.get(
#         '/events',
#         query_string='2018-11-30T21:27:14.026401Z_0.9461661960476352'
#     )

#     print(response)
#     print(response.data)
#     assert response.status_code == 200
#     assert b'event created' not in response.data


    # tmpfilepath = os.path.realpath('tmp-tesstfile')

    # def setUp(self):
    #     with open(self.tmpfilepath, 'wb') as f:
    #         f.write(b'Delete me!')

# @mock.patch('os.remove')
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


def test_get_message(client):
    response = client.get(
        '/events/messages/',
        query_string='2018-08-17T21:14:27.023732Z_0.43107498006617884'
    )
    assert response.status_code == 200
    assert b'event does not exists' in response.data


