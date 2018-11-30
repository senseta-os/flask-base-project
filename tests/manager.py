from fam.mapper import ClassMapper
from fam.database import CouchDBWrapper

from class_app import Call
from class_app import User

mapper = ClassMapper([User, Call])
db = CouchDBWrapper(
    mapper,
    'http://127.0.0.1:5984/',
    'sensitive'
)


def get_code(code):
    return db.get(code)


def create_user(user):
    return db.get(code)
