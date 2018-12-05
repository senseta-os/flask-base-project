import pytest

from cloudant.client import CouchDB

from app.providers.couchdb import CouchDBProvider
from app.main import create_app
from app.providers.user import UserCouchDBProvider
from app.providers.event import EventProvider
from app.endpoints.views import configure_views


@pytest.fixture
def app():

    app = create_app({
        'TESTING': True,
    })

    return app


def pytest_sessionstart(session):
    print('Add here before tests')


def pytest_sessionfinish(session, exitstatus):
    print('Add here after tests')
