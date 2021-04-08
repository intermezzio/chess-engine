from stockfish import Stockfish

stockfish = Stockfish("/home/intermezzio/Downloads/stockfish/stockfish_13_linux_x64_bmi2/stockfish_13_linux_x64_bmi2")

stockfish.set_position(["e2e4", "e7e6"])

print(stockfish.get_board_visual())
