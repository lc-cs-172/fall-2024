# CS2 Fall 2024 Note 38

# Running time

You can express the time taken by an algorithm as a function, such as
n³/6 − n²/2 + n/3, where n is the size of the input.

In most cases it will be clear from context what n means: the length of the
array being sorted, the number of items stored in the data structure, etc.
Running time functions usually take only one argument, but there are exceptions.

## Big O notation

Given the running time functions for two algorithms, which algorithm is faster?
This question appears to open a can of mathematical worms, but there is a huge
shortcut: asymptotic notation.  We focus on what happens as n becomes large.

It is pretty clear that n³/6 − n²/2 + n/3 when divided by n³/6 approaches 1 as
n grows.  We say that n³/6 − n²/2 + n/3 ∼ c n³, where c is a constant and n³ the
order of growth.

Common growth functions:

Order      | Nickname
-|-
O(2ⁿ)      | exponential
O(n³)      | cubic
O(n²)      | quadratic
O(n log n) | linearithmic
O(n)       | linear
O(log n)   | logarithmic
O(1)       | constant

## Activities

Answer true of false:

* 2n ∈ O(n)
* n² ∈ O(n)
* n² ∈ O(n log² n)
* n log n ∈ O(n²)

What is the order of growth of the following functions:

* 16n² + 3n + 16
* n² + 1000000n
* 3 log n
* 14 n log n/2
* 14 n + log n/2
