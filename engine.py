import chess
import random
from alt_analysis_board import AnalysisBoard
from icecream import ic
from math import inf
from random import random

ic.disable()

class CustomEngine:

    def __init__(self, board=None, strategy="alpha-beta", max_depth=4, **kwargs):
        self._board = board if board else AnalysisBoard()
        self._strategy = strategy
        self._max_depth = max_depth
        self._engine_opts = kwargs

    def __del__(self):
        del self._board

    def get_board(self):
        return self._board

    def push(self, move):
        self._board.board.push(move)

    def make_move(self, move=None, strategy=None, **kwargs):
        if move:
            self.push(move)

        strategy = strategy or self._strategy

        if strategy == "negamax":
            move = self._make_move_negamax(**kwargs)
        elif strategy == "alpha-beta":
            move = self._make_move_alpha_beta(**kwargs)

        # self._board.push(move)

        return move

    def _make_move_negamax(self, **kwargs):
        max_val, moves = self._nega_max(**kwargs)

        return moves[0]

    def _make_move_alpha_beta(self, **kwargs):
        max_val, moves = ic(self._alpha_beta_max(**kwargs))

        return moves[0]

    def _alpha_beta_max(self, alpha=-inf, beta=inf, max_depth=None) -> tuple[int, list]:
        if max_depth == 0:
            return random()-self._board.get_evaluation(), list()
        if max_depth == None:
            max_depth = self._max_depth
        if (res := self._board.board.result()) != "*":
            # game over
            if res == "1/2-1/2":
                return 0, list()
            else:
                return -(10000 + max_depth - self._max_depth), list()

        best_move = list()
        for move in self._board.board.legal_moves:
            ic(move)
            self._board.push(move)
            score, next_move = self._alpha_beta_min(alpha, beta, max_depth-1)
            score = score #+ random() # randomness is good
            self._board.pop()
            ic(score)
            ic(beta)
            if score >= beta:
                return beta, [move] + next_move
            if score > alpha:
                alpha = score
                best_move = [move] + next_move
            elif best_move == list():
                best_move = [move] + next_move

        return alpha, best_move

    def _alpha_beta_min(self, alpha=-inf, beta=inf, max_depth=None):
        if max_depth == 0:
            return random()+self._board.get_evaluation(), list()
        if max_depth is None:
            max_depth = self._max_depth
        if (res := self._board.board.result()) != "*":
            # game over
            if res == "1/2-1/2":
                return 0, list()
            else:
                return 10000 + max_depth - self._max_depth, list()

        best_move = list()
        for move in self._board.board.legal_moves:
            self._board.push(move)
            score, next_move = self._alpha_beta_max(alpha, beta, max_depth-1)
            score = score #+ random()
            self._board.pop()
            if score <= alpha:
                return alpha, [move] + next_move
            elif score < beta:
                beta = score
                best_move = [move] + next_move
            elif best_move == list():
                best_move = [move] + next_move

        return beta, best_move


    def _nega_max(self, max_depth=3) -> tuple[int, list]:
        if max_depth == 0:
            return -self._board.get_evaluation(), list()
        if max_depth == None:
            max_depth = self._max_depth
        if (res := self._board.board.result()) != "*":
            # game over
            if res == "1/2-1/2":
                return 0, list()
            else:
                return 10000 + max_depth - self._max_depth, list()

        max_val = -inf
        best_move = [None]
        for move in self._board.board.legal_moves:
            self._board.push(move)
            score, next_move = self._nega_max(max_depth-1)
            score = -score + random() # randomness is good
            self._board.pop()
            if score > max_val or best_move == [None]:
                max_val = score
                best_move = [move] + next_move

        return max_val, best_move

if __name__ == "__main__":
    c = CustomEngine()
    print(c.make_move(chess.Move.from_uci("e2e4")))
