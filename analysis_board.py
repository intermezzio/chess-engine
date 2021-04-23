import chess
import numpy as np

class AnalysisBoard(chess.Board):
	_KING_POS_EVAL   = np.genfromtxt("tables/king.csv", delimiter=",")
	_QUEEN_POS_EVAL  = np.genfromtxt("tables/queen.csv", delimiter=",")
	_ROOK_POS_EVAL   = np.genfromtxt("tables/rook.csv", delimiter=",")
	_KNIGHT_POS_EVAL = np.genfromtxt("tables/knight.csv", delimiter=",")
	_BISHOP_POS_EVAL = np.genfromtxt("tables/bishop.csv", delimiter=",")
	_PAWN_POS_EVAL   = np.genfromtxt("tables/pawn.csv", delimiter=",")
	_EVALS = [_PAWN_POS_EVAL, _KNIGHT_POS_EVAL, _BISHOP_POS_EVAL,
		_ROOK_POS_EVAL, _QUEEN_POS_EVAL, _KING_POS_EVAL]

	def __init__(self):
		super()
		self._evaluation = [0]
		self._white_pieces = dict()
		self._black_pieces = dict()

	def get_evaluation(self):
		return self._evaluation[-1]

	def push(self, move):
		## Get the piece that was moved
		## and which of the eval boards it cooresponds to
		piece = self.piece_at(move.from_square())
		color = piece.color
		pieceIndex = piece.piece_type - 1

		##Calculate what value piece had before
		## get starting index (in 0-63) from where the piece started
		startIndex = move.from_square()
		## Turn this into row and column
		row = startIndex / 8
		col = startIndex % 8
		## If ir was a black move flip them
		if not color:
			row = 8 - row
			col = 8 - col
		## Calculate what the value the piece was giving before the move was
		prevValue = _EVALS[pieceIndex][row,col]

		##Calculate value piece has now
		## get starting index (in 0-63) from where the piece ended
		endIndex = move.to_square();
		## Turn this into row and column
		row = endIndex / 8
		col = endIndex % 8
		## Calculate what the value the piece was giving after the move was
		newValue = _EVALS[pieceIndex][row,col]

		##extra value to subtract value of piece that might have been taken
		pieceTaken = self.piece_at(move.to_square())
		pieceTakenIndex = piece.piece_type - 1
		##Calculate value piece has now
		## get starting index (in 0-63) from where the piece ended
		endIndex = move.to_square()
		## Turn this into row and column
		row = endIndex / 8
		col = endIndex % 8
		takenValue = _EVALS[pieceIndex][row][col]

		## Calculate new evaluation:
			## Flip last value, add weight of new position, subtract weight
			## from last position and add value of pieces taken.
		newEval = self.get_evaluation()*-1 + newValue - prevValue + takenValue
		## add new eval.
		self._evaluation.append(newEval)
		super().push(move)
