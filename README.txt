EULER PROBLEMS
--------------
http://projecteuler.net/problems

This project contains python solution for euler problems 2,13 and 20. 

Problem 2:Even Fibonacci numbers
================================
Files:
------
euler_problem_2.py
euler_problem2_unit_test.py

Output:
-------
fibonacci_even_seq_sum took 0.02503 ms
The sum of the fibonacci sequence even valued terms not exceeding four million is 4613732

-------------------------
Why i choose this problem: 
The Fibonacci numbers are every where and it's nature's numbering system
Process Followed:
Wrote the iterative solution and then improved it further by using a python list.
http://en.wikipedia.org/wiki/Dynamic_programming
Time Spent on the problem:
~1.5 hrs which includes unit test cases and testing

Problem 13:Large sum
====================
This program requires the input file named big_num.txt that contains the 
one-hundred 50-digit numbers.

Files:
------
euler_problem_13.py
euler_problem13_unit_test.py

Output:
-------
calculate_big_sum took 0.24700 ms
The first ten digits of the sum is 5537376230 

-------------------------
Why i choose this problem: 
Mathematically not difficult,python has good support for big numbers
Process Followed:
Had to decide how to represent the list of numbers (Hard code as one big String or list of numbers)
Choose to put the list in a file and wrote the program.
Time Spent on the problem:
~1 hr which includes unit test cases and testing

Problem 20:Factorial digit sum
==============================
Files:
------
euler_problem_20.py
euler_problem20_unit_test.py

Output:
-------
factorial_digit_sum took 0.22602 ms
The sum of the digits in the number 100! is 648 

--------------------------
Why i choose this problem:
familiar with how factorial
Process Followed:
Wrote the recurive method and then improved it by using DP
http://en.wikipedia.org/wiki/Dynamic_programming
Time Spent on the problem:
~1.5 Hr which includes unit test cases and testing
