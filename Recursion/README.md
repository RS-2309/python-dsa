# Recursion

A collection of recursive algorithms implemented in Python as part of my Data Structures & Algorithms (DSA) learning journey.

The goal of this module is to understand how recursion works, recognize recursive problem patterns, and build intuition for recursive thinking before moving on to more advanced topics such as trees, divide-and-conquer algorithms, and backtracking.

---

## Files

```text
recursion.py
recursion_test.py
```

* **recursion.py** – Contains recursive implementations of common algorithms and problems.
* **recursion_test.py** – Demonstrates and tests each implementation.

---

## Topics Covered

### Basic Recursion

* Countdown
* Countup
* Sum of numbers from 1 to *n*
* Factorial

### String Problems

* Reverse a string
* Palindrome checking

### List Problems

* Recursive sum
* Recursive maximum
* Count occurrences

### Searching

* Recursive Binary Search

### Classic Recursive Problems

* Fibonacci sequence
* Power function
* Greatest Common Divisor (Euclidean Algorithm)

### Future Topics

* Permutations
* Combinations
* Backtracking
* N Queens
* Sudoku Solver

---

## Functions

| Function              | Description                                                    |
| --------------------- | -------------------------------------------------------------- |
| `countdown()`         | Prints numbers from *n* to 0 recursively.                      |
| `countup()`           | Prints numbers from 0 to *n* recursively.                      |
| `sum_to_n()`          | Returns the sum of the first *n* natural numbers.              |
| `factorial()`         | Computes the factorial of a number recursively.                |
| `reverse_string()`    | Prints a string in reverse order.                              |
| `is_palindrome()`     | Checks whether a string is a palindrome.                       |
| `recursive_sum()`     | Computes the sum of a list recursively.                        |
| `recursive_max()`     | Finds the maximum element recursively.                         |
| `count_occurrences()` | Counts occurrences of a target value recursively.              |
| `binary_search()`     | Performs recursive binary search on a sorted list.             |
| `fibonacci()`         | Computes the *n*th Fibonacci number recursively.               |
| `power()`             | Calculates exponentiation recursively.                         |
| `gcd()`               | Computes the Greatest Common Divisor using Euclid's algorithm. |

---

## Time Complexity

| Function                                    | Complexity       |
| ------------------------------------------- | ---------------- |
| Countdown                                   | O(n)             |
| Countup                                     | O(n)             |
| Sum to N                                    | O(n)             |
| Factorial                                   | O(n)             |
| Reverse String                              | O(n)             |
| Palindrome                                  | O(n)             |
| Recursive Sum                               | O(n)             |
| Recursive Max                               | O(n)             |
| Count Occurrences                           | O(n)             |
| Binary Search                               | O(log n)         |
| Fibonacci *(tail-recursive implementation)* | O(n)             |
| Power                                       | O(n)             |
| GCD                                         | O(log(min(a,b))) |

---

## Learning Objectives

This module was created to understand:

* Base cases
* Recursive calls
* Call stack behavior
* Divide-and-conquer thinking
* Recursive traversal
* Problem decomposition
* Recursive searching techniques
* Mathematical recursion