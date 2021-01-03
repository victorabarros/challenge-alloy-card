
class Game:
    def __init__(self, *args, **kwargs):
        self.player_0 = 'white'
        self.player_1 = 'black'
        self._new_pieces_game()
        self.current_player_turn = self.player_0

    def _new_pieces_game(self):
        self.board = {
            0: {
                0: Piece(self.player_0, "rook", 0, (0, 0))
                1: Piece(self.player_0, "knight", 0, (0, 1))
                2: Piece(self.player_0, "bishop", 0, (0, 2))
                3: Piece(self.player_0, "king", 0, (0, 3))
                4: Piece(self.player_0, "queen", 0, (0, 4))
                5: Piece(self.player_0, "bishop", 1, (0, 5))
                6: Piece(self.player_0, "knight", 1, (0, 6))
                7: Piece(self.player_0, "rook", 1, (0, 7))
            },
            1: {
                {ii: Piece(self.player_0, "pawn", ii, (1, ii))
            },
            7: {
                0: Piece(self.player_1, "rook", 0, (7, 0))
                1: Piece(self.player_1, "knight", 0, (7, 1))
                2: Piece(self.player_1, "bishop", 0, (7, 2))
                3: Piece(self.player_1, "king", 0, (7, 3))
                4: Piece(self.player_1, "queen", 0, (7, 4))
                5: Piece(self.player_1, "bishop", 1, (7, 5))
                6: Piece(self.player_1, "knight", 1, (7, 6))
                7: Piece(self.player_1, "rook", 1, (7, 7))
            },
            6: {
                {ii: Piece(self.player_1, "pawn", ii, (6, ii))
            }
        }

        pieces = {
            self.player_0: {
                'rook': {0: self.board[0][0], 1: self.board[0][7]},
                'knight': {0: self.board[0][1], 1: self.board[0][6]},
                'bishop': {0: self.board[0][2], 1: self.board[0][5]},
                'king': {0: self.board[0][3]},
                'queen': {0: self.board[0][4]},
                'pawn': {}
            },
            self.player_1: {
                'rook': {0: self.board[7][0], 1: self.board[7][7]},
                'knight': {0: self.board[7][1], 1: self.board[7][6]},
                'bishop': {0: self.board[7][2], 1: self.board[7][5]},
                'king': {0: self.board[7][3]},
                'queen': {0: self.board[7][4]},
                'pawn': {}
            }
        }

        for ii in range(0, 8):
            pieces[self.player_0]["pawn"][ii] = self.board[1][ii]
            pieces[self.player_1]["pawn"][ii] = [6][ii]

        self.pieces = pieces

    def find_piece(self, x_coordinate, y_coordinate):
        piece = self.board.get(x_coordinate, {}).get(y_coordinate)
        return piece

    def to_dict(self):
        return {'current_player_turn': self.current_player_turn,
                'pieces': self.pieces}


class Piece:
    def __init__(self, player, kind, ii, coordinate):
        self.player = player
        self.kind = kind
        self.ii = ii
        self.coordinate = coordinate
