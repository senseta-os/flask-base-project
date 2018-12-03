from fam.mapper import ClassMapper
from fam.database import CouchDBWrapper

from app.models.call import Call
from app.models.user import User
from app.models.event import Event


class FamProvider(object):

    def __init__(self):
        mapper = ClassMapper([User, Call, Event])
        self.db = CouchDBWrapper(
            mapper,
            'https://admin:SHFJ3QrCBNJAq8pc47LnhxBLsaAfzu@couchbk.stag.sensitve.app/',
            'sensitive'
        )
