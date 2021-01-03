from controllers.game import Game
from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

api.add_resource(Game, "/game", "/game/<string:uid>")

if __name__ == "__main__":
    app.run(port=8081, debug=True, host='0.0.0.0')
