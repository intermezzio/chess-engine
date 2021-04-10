import chess
import random

board = chess.Board()


class CustomEngine:
    def __init__(self, board=chess.Board(), color=chess.WHITE):
        self._board = board
        self._analysis = board.copy()
        self._color = color

    def make_move(self, move):
        self._board.push(move)
        self._analysis = self._board.copy()
        
        move = random.choice(list(self._analysis.legal_moves))
        self._board.push(move)
        return move

    def _evaluate_position(self, position, max_depth=4, max_candidates=5):
        for move in self.legal_moves:
            pass
        pass
