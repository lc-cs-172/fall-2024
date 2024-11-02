# CS2 Fall 2024 Note 25

## Recursion Revisited

We saw previously recursion in action with our functions, where, for instance,
`factorial` was defined in terms of itself.

```python
def factorial(n : int) -> int:
    if n == 1: return 1
    return n * factorial(n - 1)
```

Let us look at the types of the attributes of the `class Square` described in
the previous note:

```python
class Square:
    def __init__(self,
                 value : int,
                 row : list['Square'],
                 column : list['Square'],
                 block : list['Square']):
        self.value = value
        self.row = row
        self.column = column
        self.block = block
```

Notice how we are defining our new type `Square` in terms of lists of `Square`s!
Recursion is not reserved to the realm of functions; it is also very useful in
the realm of data definition.
