# Note 06

## Aliquot sequence

From the wikipedia entry about the
[Aliquot sequence](https://en.wikipedia.org/wiki/Aliquot_sequence):

> An aliquot sequence is a sequence of positive integers in which each term is
> the sum of the proper divisors of the previous term.  If the sequence reaches
> the number 1, it ends, since the sum of the proper divisors of 1 is 0.

## If statements

Some examples.  Update `max` if `x` exceeds it:

```python
if x > max:
    max = x
```

Put `x` and `y` in ascending order:

```python
if y < x:
    x, y = y, x
```

## Documentation

It is a good idea to include a docstring at the beginning of a module.  It
should describe what the module does.  By convention this docstring appears
early in the program text, before any `import` statement.

In your assignment submissions, I'd like you to include a line that identifies
who wrote the solution.  Note that this is not a standard convention in Python.

```python
"""Graph the Aliquot sequence for a positive integer n."""

__author__ = 'Jane Doe'

import matplotlib.pyplot as plt

...
```

## Functional decomposition

A long program can be greatly improved by breaking it down into multiple
functions.  This has many advantages:

* Redundant code (repeating the same statements in several places) is avoided,
  making the code shorter.
* The structure of the code is made clearer, making the code easier to read and
  write.
* Individual functions can be tested, making the code easier to debug.
* Functions can often be reused to solve other problems.

A well-designed function should do only one thing: either return a value or have
some side effect (modify a data structure in memory, draw something on the
screen, etc.).
