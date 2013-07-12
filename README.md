sudoku
======

As I sat in the runway for a delayed takeoff, I decided to fill my time with some puzzles in the back of the July 2013 American Way magazine.  It took me some time to complete the first sudoku puzzle and so I figured it may take me less time to write a program to solve the next two than solve them manually.

This code is the result of that exercise.  It ended up taking me the return flight to finish the bulk of it; all three boards are included and solved in the test suite.  I modeled the problem as a constraint satisfaction problem - which is actually how I solved the first one manually.  This involves interleaving constraint propagation and search with backtracking.

After completing my solution I researched other approaches and it turns out that mine closely matched [Peter Norvig's](http://norvig.com/sudoku.html) including variable ordering using a minimum remaining values heuristic.  However, Norvig's solution had some additional optimizations which I then adopted, particularly pre-computing peers.  I also added Norvig's noted "impossible" board to the test suite (but commented it out since it takes a long time to run). 

to run examples
---------------
After cloning:
<pre>
% cd sudoku/tests
% PYTHONPATH=.. python solver_tests.py 
</pre>

The result should be something like this:
<pre>
Original board:

. . 7 | . . . | 2 . .
. 9 3 | . 8 . | . 6 .
. 4 . | . . 9 | . . .
------+-------+------
8 . . | . . . | 4 . .
. . . | . 7 . | 1 . .
5 . 2 | . . . | . . 7
------+-------+------
. . . | . 3 . | . 8 .
. 8 . | . 6 . | 5 . .
. . . | 4 . . | 6 . .

Solution in 0.079 seconds:

1 5 7 | 3 4 6 | 2 9 8
2 9 3 | 1 8 5 | 7 6 4
6 4 8 | 7 2 9 | 3 1 5
------+-------+------
8 7 1 | 6 5 3 | 4 2 9
9 3 4 | 8 7 2 | 1 5 6
5 6 2 | 9 1 4 | 8 3 7
------+-------+------
4 1 6 | 5 3 7 | 9 8 2
7 8 9 | 2 6 1 | 5 4 3
3 2 5 | 4 9 8 | 6 7 1

.
Original board:

2 3 8 | 7 . . | . 1 9
6 . . | . . . | 7 . .
. . . | . . . | . . 5
------+-------+------
. . 2 | . 5 . | . . 7
. . . | 1 . 4 | . . .
7 . . | . 6 . | 3 . .
------+-------+------
1 . . | . . . | . . 6
. . 4 | . . . | . . 1
5 9 . | . . 7 | 8 3 4

Solution in 0.090 seconds:

2 3 8 | 7 4 5 | 6 1 9
6 4 5 | 8 9 1 | 7 2 3
9 1 7 | 6 2 3 | 4 8 5
------+-------+------
4 6 2 | 3 5 8 | 1 9 7
3 8 9 | 1 7 4 | 5 6 2
7 5 1 | 9 6 2 | 3 4 8
------+-------+------
1 7 3 | 4 8 9 | 2 5 6
8 2 4 | 5 3 6 | 9 7 1
5 9 6 | 2 1 7 | 8 3 4

.
Original board:

. . . | 6 . 3 | . . .
. 9 8 | . . . | 6 4 .
. . 6 | 5 4 . | 8 . .
------+-------+------
. . . | . . . | . 3 .
3 . 2 | . . . | 1 . 6
. 6 . | 1 . . | . . .
------+-------+------
. . 4 | . 9 1 | 7 . .
. 1 9 | . . . | 3 2 .
. . . | 7 . 5 | . . .

Solution in 0.023 seconds:

4 2 7 | 6 8 3 | 5 9 1
5 9 8 | 2 1 7 | 6 4 3
1 3 6 | 5 4 9 | 8 7 2
------+-------+------
8 7 1 | 4 5 6 | 2 3 9
3 4 2 | 9 7 8 | 1 5 6
9 6 5 | 1 3 2 | 4 8 7
------+-------+------
2 5 4 | 3 9 1 | 7 6 8
7 1 9 | 8 6 4 | 3 2 5
6 8 3 | 7 2 5 | 9 1 4

.
----------------------------------------------------------------------
Ran 3 tests in 0.196s

OK
</pre>
