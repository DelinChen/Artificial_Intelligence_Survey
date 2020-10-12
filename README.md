# Artificial Intelligence Survey
Assignments of CMPT 310 Artificial Intelligence Survey in Summer 2020.\
Languages: Python, C++

## Assignment 1: 8-puzzle and duck puzzle
- [Assignment 1 URL](https://www2.cs.sfu.ca/CourseCentral/310/tjd/a1.html)
- Some heuristic search algorithms above:
- A*-search using the misplaced tile heuristic (this is the default heuristic in the EightPuzzle class).
- A*-search using the Manhattan distance heuristic Please implement my own version of the Manhattan heuristic.
- A*-search using the max of the misplaced tile heuristic and the Manhattan distance heuristic

## Assignment 2: Ice Breaking Problem
- [Assignment 2 URL](https://www2.cs.sfu.ca/CourseCentral/310/tjd/a2.html)
- Given a group of n people, what’s the minimum number of teams they can be partitioned into such that no team has 2 (or more) members who are friends. The hope is that this encourages people to make new friends.
- Model the problem as Constraint Satisfaction Problem(CSP). Use one CSP variable for each of the n people: X1,…,Xn. The domains for these variables are team names, which will be integers 0, 1, 2, ... etc.
- All the domains are the same. The constraints on the CSP are all not-equal constraints that come from the friendship graph: if person i and j are friends, then we have the constraint Xi≠Xj, i.e. two friends cannot be on the same team.
- The problem is to find the smallest number of teams that satisfies all the constraints. In other words, we want to find the smallest domain size for the variables that satisfies all the constraints of the friendship graph.
- The word smallest is very important here. If we were satisfied with any number of teams, then we could just put each person on a team by themselves.

## Assignment 3: Tic-Tac-Toe
- [Assignment 3 URL](https://www2.cs.sfu.ca/CourseCentral/310/tjd/a3.html)
- Implement (in Python) a Tic-Tac-Toe playing program where a human can play against the computer, and the computer makes all its moves using random playouts.

## Assignment 4: Simple Knowledge Base
- [Assignment 4 URL](https://www2.cs.sfu.ca/CourseCentral/310/tjd/a4.html)
- Implement and test a definite clause theorem prover. 
- Definite clauses are a subset of the regular propositional calculus that, while not as expressive as full propositional logic, they can be used to do very efficient reasoning.

## Final Project: Fast Implementations of WalkSAT
- [Final project URL](https://www2.cs.sfu.ca/CourseCentral/310/tjd/a4.html) description within Assignment 4.
- Implement an efficient version of both WalkSAT with the minisat input format. Using the same set of test examples, compare the performance of the algorithm against the Python version of WalkSAT (in the textbook code in logic.py) and minisat. Use randomly generated k-CNF sentences as input.
- Implementation of WalkSAT using C++ (Python is probably not efficient enough).
- Randomly generated k-CNF expressions in Python, as efficiency is not as important as it is for the main solvers.
- A written report of at least one page that explains programs, the techniques they use, the results of comparisons, etc. Graphs and tables of relevant data included.
