from http import HTTPStatus
from flask_restful import Resource, reqparse
from repository import Repository
from models import Game as GameModel


class Game(Resource):
    def __init__(self):
        self._repository = Repository()

    def get(self, uid):
        # if not uid:
        #     return 404
        return self._repository.fetch(uid).to_dict(), 200

    def post(self):
        new_game = GameModel()
        uid = self._repository.insert(new_game)
        return {'uid': uid, 'game': new_game.to_dict()}, HTTPStatus.CREATED
