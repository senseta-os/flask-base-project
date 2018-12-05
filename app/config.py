import os


class Testing(object):
    TESTING = True
    DATABASE_NAME = 'test'


class Development(Testing):
    TESTING = False
    DATABASE_NAME = 'sensitive'


def load_config(app):
    FLASK_ENV = os.getenv('FLASK_ENV')

    if FLASK_ENV == 'test':
        app.config.from_object(
            'app.config.Testing'
        )
    elif FLASK_ENV == 'dev':
        app.config.from_object(
            'app.config.Development'
        )

    return app.config['DATABASE_NAME']
