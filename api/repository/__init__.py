from uuid import uuid4

DB = {}


class Repository:
    def insert(self, game):
        uid = str(uuid4())
        DB[uid] = game
        # TODO save on mongo
        return uid

    def fetch(self, uid):
        return DB.get(uid)
