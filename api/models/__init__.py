class Game:
    def __init__(self, *args, **kwargs):
        self.player_0 = 'white'
        self.player_1 = 'black'
        self.pieces = self._new_pieces_game()
        self.current_player_turn = self.player_0

    def _new_pieces_game(self):
        pieces = {
            self.player_0: {
                'rook': {0: (0, 0), 1: (0, 7)},
                'knight': {0: (0, 1), 1: (0, 6)},
                'bishop': {0: (0, 2), 1: (0, 5)},
                'king': {0: (0, 3)},
                'queen': {0: (0, 4)},
                'pawn': {}
            },
            self.player_1: {
                'rook': {0: (7, 0), 1: (7, 7)},
                'knight': {0: (7, 1), 1: (7, 6)},
                'bishop': {0: (7, 2), 1: (7, 5)},
                'king': {0: (7, 3)},
                'queen': {0: (7, 4)},
                'pawn': {}
            }
        }

        for ii in range(0, 8):
            pieces[self.player_0]["pawn"][ii] = (1, ii)
            pieces[self.player_1]["pawn"][ii] = (6, ii)

        return pieces

    def to_dict(self):
        return {'current_player_turn': self.current_player_turn,
                'pieces': self.pieces}
