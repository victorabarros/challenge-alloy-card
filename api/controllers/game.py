from http import HTTPStatus
from flask_restful import Resource, reqparse
from repository import Repository
from models import Game as GameModel
from helper.validator import MovePieceValidator


class Game(Resource):
    def __init__(self):
        self._repository = Repository()
        self._validator = MovePieceValidator()

    def post(self):
        new_game = GameModel()
        uid = self._repository.insert(new_game)
        return {'uid': uid, 'game': new_game.to_dict()}, HTTPStatus.CREATED

    def get(self, uid):
        # if not uid:
        #     return 404
        return self._repository.fetch(uid).to_dict(), 200

    def patch(self, uid):
        req = reqparse.request
        body = req.get_json()

        success, errors = self._validator.validate(body)
        if not success:
            return {"errors": errors}, HTTPStatus.BAD_REQUEST

        game = self._repository.fetch(uid)

        if body['player'] != game.current_player_turn:
            # return 404
            pass

        piece = game.find_piece_at(*body['currentCoordinate'])
        if body['piece'] != piece.kind:
            # return 404
            pass

        # TODO
        # game.move(body['piece'], body['currentCoordinate'], body['moveTo'])
