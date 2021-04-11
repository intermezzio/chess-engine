---
title: Final Project Proposal
subtitle: Checkmatr - The DSA Chess Engine
author: Andrew Mascillaro, Nabih Estefan

---

# About the Project

This is an implementation-based project for
the Olin College Spring 2021 Data Structures
and Algorithms class. This project will
attempt to create a strong and efficient
chess engine using dynamic programming and 
properties of game trees explored in the class.

This project will use the `chess` library in Python
for finding legal moves and otherwise moving the pieces
for the algorithm. Custom functions, which will
attempt to evaluate a chess position based on
multiple factors, will be used to determine the 
best move at any given time. These functions will
be determined from background research and
chess intuition.

To test the strength of this algorithm, it will
play against Stockfish's API at varying rating levels
to determine the engine's theoretical rating.

# Timeline

## MVP

* Install dependencies and set up environment
**Done**
* Create an extended chess board class with
precalculated evaluations of static positions
(so that it can be quickly updated at each move instead
of recalculated) **April 12**
* Create a first pass breadth first search algorithm **April 15**

## First Stretch

* Modify this algorithm with more complex analysis **April 22**
* Test with Stockfish and determine rating **April 25**

## Second Stretch

* Create multiple levels of difficulty (more depth, etc)
which can be configured on demand **May 2**
* Allow a user to play the engine from the command line
**May 2**

## Third Stretch (Mostly Optional, Dates Not Applicable)

* Create a GUI or web server for playing the engine
* Convert it to JavaScript for client side playing
* Allow it to continuously search deeper and display
an ongoing prediction of its best lines

# References

[**A Step-by-step Guide to Making a Chess AI (link)**](https://www.freecodecamp.org/news/simple-chess-ai-step-by-step-1d55a9266977/)  
This has some basic information on how to evaluate a static position
based only on the position of the pieces. It's pretty trash
but a good first pass algorithm.

[**AI Chess Algorithms (link)**](https://www.cs.cornell.edu/boom/2004sp/ProjectArch/Chess/algorithms.html)  
This is a more in-depth analysis of a chess engine
done by a Cornell graduate student. The more complex
features of chess positions this takes into account
can be used to make a more powerful chess engine.
