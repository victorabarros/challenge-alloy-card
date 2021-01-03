from http import HTTPStatus
from flask_restful import Resource, reqparse
from repository import Repository
from models import Game as GameModel


class Game(Resource):
    def __init__(self):
        self._repository = Repository()

    def post(self):
        request = reqparse.request
        body = request.get_json() or {}  # TODO move to validation

        # success, errors = self._validator.validate(body)
        # if not success:
        #     return {"errors": errors}, HTTPStatus.BAD_REQUEST

        new_game = GameModel(**body)

        try:
            uid = self._repository.insert(new_game)
        except Exception:
            # TODO
            pass

        return {'uid': uid, 'game': new_game.to_dict()}, HTTPStatus.CREATED
