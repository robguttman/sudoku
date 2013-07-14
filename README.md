sudoku
======

As I sat in the runway for a delayed takeoff, I decided to fill my time with some puzzles in the back of the July 2013 American Way magazine.  It took me some time to complete the first sudoku puzzle and so I figured it may take me less time to write a program to solve the next two than solve them manually.

This code is the result of that exercise.  It ended up taking me the return flight to finish the bulk of it; all three boards are included and solved in the test suite.  I modeled the problem as a constraint satisfaction problem - which is actually how I solved the first one manually.  This involves interleaving constraint propagation and search with backtracking.

After completing my solution I researched other approaches and it turns out that mine closely matched [Peter Norvig's](http://norvig.com/sudoku.html) including variable ordering using a minimum remaining values heuristic.  However, Norvig's solution had some additional optimizations which I then adopted, particularly pre-computing peers.  I also added a few of Norvig's example boards to the test suite (but commented it the "hard" one since it takes a long time to run). 

to run examples
---------------
After cloning:
<pre>
% cd sudoku/tests
% PYTHONPATH=.. python solver_tests.py
</pre>

The result should be something like this:
<pre>
Original board (diabolical):

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

Solution in 0.059 seconds:

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
Original board (easy):

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

Solution in 0.066 seconds:

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
Original board (inkala1):

8 5 . | . . 2 | 4 . .
7 2 . | . . . | . . 9
. . 4 | . . . | . . .
------+-------+------
. . . | 1 . 7 | . . 2
3 . 5 | . . . | 9 . .
. 4 . | . . . | . . .
------+-------+------
. . . | . 8 . | . 7 .
. 1 7 | . . . | . . .
. . . | . 3 6 | . 4 .

Solution in 2.544 seconds:

8 5 9 | 6 1 2 | 4 3 7
7 2 3 | 8 5 4 | 1 6 9
1 6 4 | 3 7 9 | 5 2 8
------+-------+------
9 8 6 | 1 4 7 | 3 5 2
3 7 5 | 2 6 8 | 9 1 4
2 4 1 | 5 9 3 | 7 8 6
------+-------+------
4 3 2 | 9 8 1 | 6 7 5
6 1 7 | 4 2 5 | 8 9 3
5 9 8 | 7 3 6 | 2 4 1

.
Original board (inkala2):

. . 5 | 3 . . | . . .
8 . . | . . . | . 2 .
. 7 . | . 1 . | 5 . .
------+-------+------
4 . . | . . 5 | 3 . .
. 1 . | . 7 . | . . 6
. . 3 | 2 . . | . 8 .
------+-------+------
. 6 . | 5 . . | . . 9
. . 4 | . . . | . 3 .
. . . | . . 9 | 7 . .

Solution in 0.216 seconds:

1 4 5 | 3 2 7 | 6 9 8
8 3 9 | 6 5 4 | 1 2 7
6 7 2 | 9 1 8 | 5 4 3
------+-------+------
4 9 6 | 1 8 5 | 3 7 2
2 1 8 | 4 7 3 | 9 5 6
7 5 3 | 2 9 6 | 4 8 1
------+-------+------
3 6 7 | 5 4 2 | 8 1 9
9 8 4 | 7 6 1 | 2 3 5
5 2 1 | 8 3 9 | 7 6 4

.
Original board (moderate):

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

Solution in 0.016 seconds:

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
Original board (norvig):

4 . . | . . . | 8 . 5
. 3 . | . . . | . . .
. . . | 7 . . | . . .
------+-------+------
. 2 . | . . . | . 6 .
. . . | . 8 . | 4 . .
. . . | . 1 . | . . .
------+-------+------
. . . | 6 . 3 | . 7 .
5 . . | 2 . . | . . .
1 . 4 | . . . | . . .

Solution in 0.481 seconds:

4 1 7 | 3 6 9 | 8 2 5
6 3 2 | 1 5 8 | 9 4 7
9 5 8 | 7 2 4 | 3 1 6
------+-------+------
8 2 5 | 4 3 7 | 1 6 9
7 9 1 | 5 8 6 | 4 3 2
3 4 6 | 9 1 2 | 7 5 8
------+-------+------
2 8 9 | 6 4 3 | 5 7 1
5 7 3 | 2 9 1 | 6 8 4
1 6 4 | 8 7 5 | 2 9 3

.
----------------------------------------------------------------------
Ran 6 tests in 3.390s

OK
</pre>
