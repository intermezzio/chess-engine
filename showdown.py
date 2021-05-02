import argparse
from stockfish import Stockfish
import chess
import chess.pgn
from engine import CustomEngine
import re

def match(white="stockfish", black="custom", elo=None, name="Python Chess",
		strategy="alpha-beta", max_depth=5, disp=True):
	game = chess.pgn.Game()
	game.headers["Event"] = name
	players = list()
	player_names = [white, black]
	if white == "stockfish":
		players.append(Stockfish("/usr/bin/stockfish"))
		if elo:
			players[0].set_elo_rating(elo)
			game.headers["White"] = f"Stockfish {elo} Elo"
		else:
			game.headers["White"] = "Stockfish"
	elif white == "custom":
		players.append(CustomEngine(max_depth=max_depth))
		game.headers["White"] = f"Custom {strategy} Engine (depth {max_depth})"
	else:
		players.append(None)
		game.headers["White"] = input("What is your name? ")

	if black == "stockfish":
		players.append(Stockfish("/usr/bin/stockfish"))
		if elo:
			players[1].set_elo_rating(elo)
			game.headers["Black"] = f"Stockfish {elo} Elo"
		else:
			game.headers["Black"] = "Stockfish"
	elif black == "custom":
		players.append(CustomEngine(max_depth=max_depth))
		game.headers["Black"] = f"Custom {strategy} Engine (depth {max_depth})"
	else:
		players.append(None)
		game.headers["Black"] = input("What is your name? ")

	official_board = chess.Board()

	black_to_move = False
	if disp:
		print(official_board)
	while official_board.result() == "*":
		player = player_names[black_to_move]
		engine = players[black_to_move]
		move = make_move(engine=engine, player=player, board=official_board)

		black_to_move = not black_to_move

		print(official_board.san(move))
		official_board.push(move)
		if disp:
			print(official_board)

		push_move(move, official_board.fen(), engine=players[0], player=player_names[0])
		push_move(move, official_board.fen(), engine=players[1], player=player_names[1])


	game.headers["Outcome"] = res = official_board.result()
	print(official_board.result())
	game.add_line(official_board.move_stack)
	with open(f"games/{snake(name)}.pgn", "w") as outfile:
		outfile.write(str(game))

	del players

	if res == "1-0":
		return 1.0
	elif res == "1/2-1/2":
		return 0.5
	elif res == "0-1":
		return 0.
	else:
		print(res)
		return -1
def make_move(engine=None, player="stockfish", board=None):
	if player == "stockfish":
		move_str = engine.get_best_move()
		move = chess.Move.from_uci(move_str)
	elif player == "custom":
		move = engine.make_move()
	elif player == "human":
		move = make_player_move(board)
	return move

def push_move(move, fen, engine=None, player="stockfish"):
	if player == "stockfish":
		engine.set_fen_position(fen)
	elif player == "custom":
		engine.push(move)

def snake(name):
	"""Convert name to snake case for filename"""
	name = re.sub(r'\W+', ' ', name)
	name = re.sub('(.) ([A-Z][a-z]+)', r'\1_\2', name)
	return re.sub('([a-z0-9]) ([A-Z])', r'\1_\2', name).lower().strip()

def make_player_move(board):
	"""Ask a human to make a move"""
	move_str = input("Make a move: ")
	try:
		move = board.parse_san(move_str)
		assert move in board.legal_moves
	except ValueError as e:
		print("What is this gibberish?")
		# print(e)
		return make_player_move(board)
	except AssertionError:
		print("I meant a legal move")
		return make_player_move(board)

	return move

if __name__ == "__main__":
	match(white="stockfish", black="human", elo=5000) # name="Andrew tries to play the engine")
