import os
from flask import Flask
from flask import render_template
from flask_injector import FlaskInjector

from cloudant.client import CouchDB

from app.providers.couchdb import CouchDBProvider
from app.providers.user import UserCouchDBProvider
# from app.providers.user import UserFamProvider
from app.providers.event import EventProvider

from app.endpoints.views import configure_views


def create_app(test_config=None):
    app = Flask(__name__)
    # create and configure the app
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def visit_home(name=None):
        return render_template('/index.html', name=name)

    configure_views(app)

    def configure(binder):
        client = CouchDB(
            user='admin',
            auth_token='SHFJ3QrCBNJAq8pc47LnhxBLsaAfzu',
            url='https://couchbk.stag.sensitve.app',
            connect=True
        )
        provider = CouchDBProvider(client, app.config['NAME'])
        binder.bind(CouchDB, to=client)
        binder.bind(CouchDBProvider, to=provider)
        binder.bind(UserCouchDBProvider)
        binder.bind(EventProvider)

    FlaskInjector(app=app, modules=[configure])

    return app
