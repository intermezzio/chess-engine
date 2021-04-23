# from stockfish import Stockfish

# stockfish = Stockfish("/home/intermezzio/Downloads/stockfish/stockfish_13_linux_x64_bmi2/stockfish_13_linux_x64_bmi2")

# stockfish.set_position(["e2e4", "e7e6"])

# print(stockfish.get_board_visual())

import asyncio
import chess
import chess.engine
import chess.pgn
from engine import CustomEngine

async def main() -> None:
    transport, engine = await chess.engine.popen_uci("/usr/bin/stockfish")
    
    dsa_engine = CustomEngine(color=chess.BLACK)

    board = chess.Board()

    while not board.is_game_over():
        result = await engine.play(board, chess.engine.Limit(time=0.1))
        
        print(board.san(result.move))
        
        board.push(result.move)
        
        print(board)
        
        if not board.is_game_over():
        	new_move = dsa_engine.make_move(result.move)
        	board.push(new_move)


    # await 
    await engine.quit()
    game = chess.pgn.Game()
    game.add_line(board.move_stack)
    with open("games/new.pgn", "w") as outfile:
    	outfile.write(str(game))

asyncio.set_event_loop_policy(chess.engine.EventLoopPolicy())
asyncio.run(main())