# CS2 Fall 2024 Note 15

## Review

### References

Draw the diagram for the memory representation of the list below:

```python
x = [0.00, 3.14, 2.72, 1.41]
```

### Calling stack

Draw the calling stack as the function `main` executes.  Draw the stack at each
of the "execution points" (1, 3, 5, 4, 2) noted in the program below.

```python
def b(x):
    # 5
    return x + 1

def a(x):
    # 3
    r = b(x)
    # 4
    return r

main():
    # 1
    r = a(10)
    # 2
    print(r)
```

How is calling stack changing with the program below.

```python
def b(x, y):
    # 5
    return x + y

def a(x, y):
    # 3
    r = b(x, y)
    # 4
    return r

main():
    # 1
    r = a(10, 20)
    # 2
    print(r)
```

### Conversions

How do you convert a value into a string?

How do you convert a string into an integer?

How do you convert a string into a `float`?

How do you convert a `float` to the nearest integer?

How do you get the ASCII code of a character?

How do you get the character corresponding to a particular ASCII code?

What is the maximum value of an `int`?

### Collections

How do you initialize a set with the elements 1, 2, 3?

Does the order of elements in the set literal matter?

How do you initialize a tuple with the elements 1, 2, 3, in that order?

How do you check for membership in a set?

How do you add and remove an element from a set?

Do sets allow duplicates?

Do tuples allow duplicates?

### Testing

What is the naming convention of test functions in a `pytest` test module?

What claim does the following assertion make?

```python
assert square(4) == 16
```
