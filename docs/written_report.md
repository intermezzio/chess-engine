---
title: Checkmatr Written Report
author: Andrew Mascillaro, Nabih Estefan

---

# Overview

Chess has simple rules, but the game
space is extremely large. With the strength
of our current computers, we aren't even
close to solving the game of chess by brute force.
As a fallback, engines use a heuristic to
try to find the best moves for a given player,
which basically traverses a "game tree" (tree 
of possible moves for both players) and quantitatively
evaluates the resulting position. This project
primarily focuses on how to efficiently
traverse such a game tree and create an effective
heuristic to maximize the strength of a chess engine.
To test the engine's strength, we have scripts
that allow the engine to play agains humans or Stockfish (a top
open source chess engine) at different rating levels.
Our engine outperformed our expectations, and has
won games against the 2200 rated Stockfish engine,
which basically means this engine is strong enough
to be a titled player in the chess world.

# Background Information

## Game Tree Traversal

### Minimax

The most basic tree traversal is a minimax
algorithm. This algorithm assumes that white
and black will play their optimal moves and
tries to find the most favorable move
_assuming that both players play perfectly_.
Essentially it is a depth first search
at a fixed depth, and once that depth is
reached, a static evaluation of the position
is calculated.
More information can be found [**here**](https://www.chessprogramming.org/Minimax).
While the space complexity of this is negligible,
the time complexity is $m^p$, where each
player has roughly $m$ moves per ply $p$ (a
ply is half of a move or just one turn for one
player). The proof for this is explained in
the linked research.

### Alpha Beta Pruning

A standard minimax traversal can be very slow,
so shortcuts are very useful. 
Alpha beta pruning stops traversing a portion
of the game tree that is already known to be
bad. For example, if white makes a move that
is pretty good, then it doesn't have to
go into detail analyzing lines where it loses
a piece because that move is already proven
inferior. By skipping these inferior lines,
the new average runtime is estimated to be
$\sqrt{m^p}$, which can be seen in
[**this research**](https://www.chessprogramming.org/Alpha-Beta).

### ProbCut

This algorithm takes Alpha Beta pruning
to the next level by avoiding portions
of the gamespace that "probably" won't be
the best line. For example, if a good move has
already been found and the current move
being observed seems worse *but isn't
proven to be worse than other moves*, ProbCut
can still choose to stop checking that move.
This makes ProbCut a lot faster, but when it's done
at the same depth as Alpha Beta pruning, it may
perform slightly worse. The benefit, though, is
that faster algorithms can go much deeper in
their searches in the same amount of time,
so a faster search (even if it's less accurate)
can actually be a lot better. More info about
the ProbCut algorithm can be found [**here**](https://www.chessprogramming.org/ProbCut).

## Positional and Material Heuristic



## Endgame Tablebases as a Heuristic

# Our Implementation

Our project involved creating a python script that
plays chess against itself, Stockfish, and human opponents.
We created a custom class for storing a board and its
heuristic updated in real time, as well as an engine
class that can traverse the tree using any implemented algorithm
at a custom depth.

## What we can do

We built an algorithm that uses minimax
and another algorithm that uses alpha beta
pruning for move prediction. A minimax approach
of depth 3 is as fast as an alpha-beta approach
of depth 4, which shows how our alpha-beta approach
is significantly faster.

We have a heuristic that constantly updates when a new
move is made. Because our heuristic is purely focused
on material and positioning of pieces, this allows us to use
the existing heuristic and only change the moved piece's
evaluation when updating the new heuristic. This saves the
algorithm a lot of time.

Our algorithm has played a variety of games, many
of which are stored in the `games/` folder of the project
repostory as PGN files. It has beat Stockfish in a variety of games
as shown in ~~results~~.

