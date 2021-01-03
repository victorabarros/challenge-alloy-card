from uuid import uuid4


class Repository:
    def __init__(self):
        self._db = {}

    def insert(self, game):
        uid = uuid4().__str__()
        self._db[uid] = game
        # TODO save on mongo
        return uid
