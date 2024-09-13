# Note 05

## Omitting needless code

Let us study [this](https://codingbat.com/prob/p173401) CodingBat exercise:

`Warmup-1 > sleep_in`

The parameter `weekday` is `True` if it is a weekday, and the parameter
`vacation` is `True` if we are on vacation.  We sleep in if it is not a weekday
or we're on vacation.  Return `True` if we sleep in.

```
sleep_in(False, False) → True
sleep_in(True, False) → False
sleep_in(False, True) → True
```

## Lists

Lists are a fundamental data collection supported in Python.  Lists in Python
share characteristics of C arrays and lists as supported in functional
languages (such as Lisp and Haskell).

### Examples

```python
a = []                  # an empty list
a = [1, 2, 3]           # a list of whole numbers
a = [1., 2., 3.]        # a list of floats
a = ['a', 'ab', 'abc']  # a list of strings
a.append('abcd')        # add an element at the end
a.pop()                 # remove the last element
a[2]                    # access the third element (zero-based index)
a[-2]                   # access the second element from the end
a[2] = 'xyz'            # replace the content of the third element

# list of lists
a = [ ['a', 'b', 'c'], ['x', 'y', 'z'] ]

# can be used to hold arrays
a = [
        [ 1.0,  2.0,  3.0],
        [ 4.0,  5.0,  6.0],
        [ 7.0,  8.0,  9.0],
        [10.0, 11.0, 12.0]
    ]
```

## Slices

A slice is a copy of a contiguous sequence of elements from a source list.  The
syntax is `a[i:j]` where `a` is the source list.  This expression returns a new
list with elements `a[i]`, `a[i + 1]`, ..., `a[j - 1]`.  If you do not specify
`i`, it defaults to `0`; if you do not specify `j`, it defaults to `len(a)`.

### Examples

```python
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a[2:6]                   # [2, 3, 4, 5]
a[7:]                    # [7, 8, 9]
a[:3]                    # [0, 1, 2]
a[2:-2]                  # [2, 3, 4, 5, 6, 7]
a[:]                     # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```
