# sudoku solvers
This repo contains two sudoku solvers: brute force(also known as backtracking) and one solved by simulated annealing.

Usage of simulated annealing:

```
usage: simulated_annealing.py [-h] [--f F] [--t T] [--tdr TDR] [--maxiter MAXITER]

optional arguments:
  -h, --help         show this help message and exit
  --f F              File with sudoku puzzle
  --t T              Initial temperature
  --tdr TDR          Temperature decrease rate
  --maxiter MAXITER  Max number of iterations

```

Execution example:

```

(base) C:\Users\gekas\sudoku> python simulated_annealing.py --f sudoku3.txt
[Iteration 0] current score: 45, best score: 45
[Iteration 1000] current score: 8, best score: 8
[Iteration 2000] current score: 6, best score: 6
[Iteration 3000] current score: 8, best score: 6
[Iteration 4000] current score: 4, best score: 2
[Iteration 5000] current score: 2, best score: 2
[Iteration 6000] current score: 3, best score: 2
[Iteration 7000] current score: 3, best score: 2
Solution found!
[[5 3 4 6 7 8 9 1 2]
 [6 7 2 1 9 5 3 4 8]
 [1 9 8 3 4 2 5 6 7]
 [8 5 9 7 6 1 4 2 3]
 [4 2 6 8 5 3 7 9 1]
 [7 1 3 9 2 4 8 5 6]
 [9 6 1 5 3 7 2 8 4]
 [2 8 7 4 1 9 6 3 5]
 [3 4 5 2 8 6 1 7 9]]

```

Used sources:

[1] Overall understanding of math of simulated annealing: [https://de.wikipedia.org/wiki/Simulated_Annealing](https://de.wikipedia.org/wiki/Simulated_Annealing)

[2] More specific details of simulated annealing: [https://github.com/erichowens/SudokuSolver](https://github.com/erichowens/SudokuSolver)