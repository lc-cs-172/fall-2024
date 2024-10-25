# CS2 Fall 2024 Note 22

## Ordered pairs

An ordered pair is another name for a 2-tuple, a comma-separated sequence of
two values.  Recall that you can create such a pair with an expression like
`(43, -5)`.  The two values need not be of the same type.  Here is that
expression assigned to a variable:

```python
pair = (43, -5)
```

You can access specific members of a tuple with an index.

```python
pair[0]  # first value in the tuple
pair[1]  # second value in the tuple
```

## Objects and classes

Every value in Python is an object.  For example, the int `5`, the list
`[1, 2, 3]`, and the string `'hello'` are all objects.

Every object is an instance of some *class* (also known as a type).

You can create your own type.  Here is a draft of the `Square` class:

```python
class Square:
    pass
```

By convention, class names start with upper-case letters.  The keyword `pass`
just indicates that, for the moment, the body of the class definition is empty.

You can now create an instance of `Square`:

```python
s = Square()
```

### Attributes

You can add values called attributes to an object.  Continuing the previous
example:

```python
s.value = 0
s.row = [None]*8
s.column = [None]*8
s.block = [None]*8
```

Now you can use `s.value` or `s.column` anywhere you want to know about these
values, but you can use `s` to refer to the entire `Square`.  This ability to
refer to a whole collection of named values (and, for example, pass it into or
return it from a function) is a key feature of objects.

Each instance of the `Square` class can have its own values for these
attributes.  If you define:

```python
t = Square()
t.value = 7
t.row = [None]*8
t.column = [None]*8
t.block = [None]*8
```

then `s.value` is `0` but `t.value` is `7`.
