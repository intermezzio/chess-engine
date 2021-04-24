import chess
import numpy as np
from icecream import ic
from random import random

class AnalysisBoard:
	_KING_POS_EVAL   = np.genfromtxt("tables/king.csv", delimiter=",")
	_QUEEN_POS_EVAL  = np.genfromtxt("tables/queen.csv", delimiter=",")
	_ROOK_POS_EVAL   = np.genfromtxt("tables/rook.csv", delimiter=",")
	_KNIGHT_POS_EVAL = np.genfromtxt("tables/knight.csv", delimiter=",")
	_BISHOP_POS_EVAL = np.genfromtxt("tables/bishop.csv", delimiter=",")
	_PAWN_POS_EVAL   = np.genfromtxt("tables/pawn.csv", delimiter=",")
	_EVALS = [_PAWN_POS_EVAL, _KNIGHT_POS_EVAL, _BISHOP_POS_EVAL,
		_ROOK_POS_EVAL, _QUEEN_POS_EVAL, _KING_POS_EVAL]
	_VALUES = [10, 30, 30, 50, 90, 900]

	def __init__(self):
		self._evaluation = [0]
		self._white_pieces = dict()
		self._black_pieces = dict()
		self.board = chess.Board()

	def get_evaluation(self):
		return self._evaluation[-1]

	def push(self, move):
		if self.board.is_castling(move):
			newEval = self.get_evaluation*-1 + 3 + 0
		else:
			try:
				## Get the piece that was moved
				## and which of the eval boards it cooresponds to
				piece = self.board.piece_at(move.from_square)
				color = piece.color
				pieceIndex = piece.piece_type - 1

				##Calculate what value piece had before
				## get starting index (in 0-63) from where the piece started
				startIndex = move.from_square
				## Turn this into row and column
				row = startIndex // 8
				col = startIndex % 8
				## If ir was a black move flip them
				if color:
					row = 7 - row
					col = 7 - col
				## Calculate what the value the piece was giving before the move was
				prevValue = self._EVALS[pieceIndex][row][col]
				# print("prev value:", prevValue)
				##Calculate value piece has now
				## get starting index (in 0-63) from where the piece ended
				endIndex = move.to_square
				## Turn this into row and column
				row = endIndex // 8
				col = endIndex % 8
				if color:
					row = 7 - row
					col = 7 - col
				## Calculate what the value the piece was giving after the move was
				newValue = self._EVALS[pieceIndex][row,col]
				# print("new value:", newValue)

				##extra value to subtract value of piece that might have been taken
				pieceTaken = self.board.piece_at(move.to_square)
				# print("piece taken:", pieceTaken)
				if pieceTaken:
					pieceTakenIndex = pieceTaken.piece_type - 1
					# print("pieceTakenIndex", pieceTakenIndex)
					##Calculate value piece has now
					## get starting index (in 0-63) from where the piece ended

					endIndex = move.to_square
					## Turn this into row and column
					row = endIndex // 8
					col = endIndex % 8
					if not color:
						row = 7 - row
						col = 7 - col
					takenValue = self._EVALS[pieceTakenIndex][row][col] + \
						self._VALUES[pieceTakenIndex]
				elif self.board.is_en_passant(move):
					pieceTakenIndex = chess.PAWN - 1
					# print("pieceTakenIndex", pieceTakenIndex)
					##Calculate value piece has now
					## get starting index (in 0-63) from where the piece ended
					startIndex = move.from_square
					endIndex = move.to_square
					## Turn this into row and column
					row = startIndex // 8
					col = endIndex % 8
					if not color:
						row = 7 - row
						col = 7 - col
					takenValue = self._EVALS[pieceTakenIndex][row][col] + \
						self._VALUES[pieceTakenIndex]

				else:
					takenValue = 0

				# print("takenvalue:", takenValue)
				## Calculate new evaluation:
					## Flip last value, add weight of new position, subtract weight
					## from last position and add value of pieces taken.

				newEval = self.get_evaluation()*-1 + newValue - prevValue + takenValue
				## add new eval.
			except Exception as e:
				print(e)
				newEval = -self.get_evaluation()
		self._evaluation.append(newEval)
		self.board.push(move)

	def pop(self):
		del self._evaluation[-1]
		self.board.pop()

if __name__ == "__main__":
	x = AnalysisBoard()
	x.push(next(iter(x.board.legal_moves)))
	ic(x.get_evaluation())
	x.push(chess.Move.from_uci("g7g5"))
	ic(x.get_evaluation())
	x.push(chess.Move.from_uci("h3g5"))
	ic(x.get_evaluation())
	x.push(chess.Move.from_uci("f8g7"))
	ic(x.get_evaluation())
	x.push(chess.Move.from_uci("e2e4"))
