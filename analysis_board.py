import chess
import numpy as np

class AnalysisBoard(chess.Board):
	_KING_POS_EVAL   = np.genfromtxt("tables/king.csv", delimiter=",")
	_QUEEN_POS_EVAL  = np.genfromtxt("tables/queen.csv", delimiter=",")
	_ROOK_POS_EVAL   = np.genfromtxt("tables/rook.csv", delimiter=",")
	_KNIGHT_POS_EVAL = np.genfromtxt("tables/knight.csv", delimiter=",")
	_BISHOP_POS_EVAL = np.genfromtxt("tables/bishop.csv", delimiter=",")
	_PAWN_POS_EVAL   = np.genfromtxt("tables/pawn.csv", delimiter=",")

	def __init__(self):
		super()
		self._evaluation = 0
		self._white_pieces = dict()
		self._black_pieces = dict()

	def get_evaluation(self):
		return self._evaluation

	def _calculate_static(self):
		pass