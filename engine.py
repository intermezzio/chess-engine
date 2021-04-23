import chess
import random
from alt_analysis_board import AnalysisBoard
from icecream import ic
from random import random

board = chess.Board()


class CustomEngine:
    def __init__(self, board=AnalysisBoard(), color=chess.WHITE):
        self._board = board
        self._color = color

    def make_move(self, move=None):
        if move:
            self._board.push(move)
        # self._analysis = self._board.copy()
        
        max_val, moves = self._nega_max(3)

        self._board.push(moves[0])
        return moves[0]

    def _evaluate_position(self, position, max_depth=4, max_candidates=5):
        for move in self.legal_moves:
            pass
        pass

    def _nega_max(self, max_depth=3) -> tuple[int, list]:
        if max_depth == 0:
            return self._board.get_evaluation(), list()
        
        max_val = float('inf')
        best_move = [None]
        for move in self._board.board.legal_moves:
            self._board.push(move)
            score, next_move = self._nega_max(max_depth-1)
            score = -score + random() # randomness is good
            self._board.pop()
            if score < max_val or best_move == [None]:
                max_val = score
                best_move = [move] + next_move

        return max_val, best_move