sudoku
======

As I sat in the runway for a delayed takeoff, I decided to fill my time with some puzzles in the back of the July 2013 American Way magazine.  It took me some time to complete the first sudoku puzzle and so I figured it may take me less time to write a program to solve the next two for me than solve them myself.

This code is the result of that exercise.  It ended up taking me the return flight to finish the bulk of it.  I modeled the problem as a constraint satisfaction problem - which is actually how I solved the first one manually.

After completing my solution I researched other approaches and it turns out that mine closely matches [Peter Norvig's](http://norvig.com/sudoku.html)* including variable ordering.  However, Norvig's solution had some additional performance optimizations which I then adopted, particularly pre-computing peers.
