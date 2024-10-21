# CS2 Fall 2024 Note 20

## Harmonic series

```python
def harmonic(n : int) -> float:
    """Return the sum of the first n term of the harmonic series."""
    if n == 1: return 1.0
    return harmonic(n - 1) + 1.0/n
```

## Fibonacci sequence

```python
def fib(n : int) -> int:
    """Return the nth member of the Fibonacci sequence."""
    if n == 0: return 0
    if n == 1: return 1
    return fib(n - 1) + fib(n - 2)
```

## Pitfalls of recursion

* Missing base case
* No guarantee of convergence
* Excessive recomputation
* Excessive memory requirements

## Call graph

According to [this](https://en.wikipedia.org/wiki/Call_graph) Wikipedia article,
a *call graph* [...] represents the relationships between functions in a
computer program.

## Dictionary

In computer science, a
[dictionary](https://en.wikipedia.org/wiki/Associative_array) (also called
associative array, map, or symbol table) stores a collection of (key, value)
pairs, such that each possible key appears at most once in the collection.  In
mathematical terms, a dictionary is a function with finite domain.

Python supports
[dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries).
Here are a few examples taken from the documentation:

```python
tel = {'jack': 4098, 'sape': 4139}  # initialization
tel['guido'] = 4127                 # insertion
tel['jack']                         # lookup
del tel['sape']                     # deletion
```
