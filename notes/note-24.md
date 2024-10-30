# CS2 Fall 2024 Note 24

## Objects

Last week we saw how to declare a new type (or class):

```python
class Square:
    pass
```

How to create an instance (or object) of that new type/class:

```python
s = Square()
```

How to assign this instance/object some attributes:

```python
s.value = 0
s.row = [None]*8
s.column = [None]*8
s.block = [None]*8
```

We can access these attributes individually:

```python
s.value
s.row
```

But we can also refer to the entire content of the object with `s`.  For
instance, in the third group assignment, I'm asking you to write the following
function:

```python
def find_valid_numbers(square : Square) -> list[bool]:
    """Returns a boolean array of length 10.  For each digit, the
    corresponding entry in the array is `True` if that number does not
    appear elsewhere in the `Square`'s row, column, or block."""
```

This function takes as an argument an object of type `Square` which includes
the attributes `value`, `row`, `column` and `block`.

### Initializers

Rather than attaching the attributes after the fact, it would be nicer to be
able to specify them when you create the object:

```python
s = Square(0, [None]*8, [None]*8, [None]*8)
```

You can do this by defining an initializer inside the class.  Here's the
improved version of `Square` (do not use this improved version in the third
group assignment):

```python
class Square:
    def __init__(self, value, row, column, block):
        self.value = value
        self.row = row
        self.column = column
        self.block = block
```
