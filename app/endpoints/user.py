from flask.views import MethodView
from flask import request
from injector import inject

from app.providers.user import UserCouchDBProvider


class UserAPI(MethodView):

    @inject
    def __init__(self, user_provider: UserCouchDBProvider):
        self.user = user_provider

    def get(self):
        return 'hello'

    def post(self):
        new_user = self.user.create_user(
            name=request.form['name'],
            phone=request.form['phone'],
            email=request.form['email'],
            birth=request.form['birth']
        )

        return str(new_user)
