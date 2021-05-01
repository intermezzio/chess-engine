import pandas as pd
from itertools import cycle, count
import time
from showdown import match


def multi(iterator, n=4):
    while val := next(iterator):
        for _ in range(n):
            yield val
def print_through(iterator):
    while val := next(iterator):
        print(val)
        yield val

players = cycle((("custom", "stockfish"), ("stockfish", "custom")))
elo = multi(count(1200, 400))
games_df = pd.DataFrame(columns=["white", "black", "elo", "result", "adj_result", "name"])

if __name__ == "__main__":
    rolling_results = [1] * 5
    for (white, black), elo in print_through(zip(players, elo)):
        name = str(int(time.time()))
        result = match(white=white, black=black, elo=elo, name=name, disp=False)

        if black == "custom":
            adj_result = 1 - result
        else:
            adj_result = result

        games_df = games_df.append({
            "name": "games/" + name + ".pgn",
            "result": result,
            "adj_result": adj_result,
            "white": white,
            "black": black,
            "elo": elo
        }, ignore_index=True)
        rolling_results = rolling_results[1:] + [adj_result]
        if sum(rolling_results) < 1:
            break

    games_df.to_csv("batch_results.csv", index=False)
