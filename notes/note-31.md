# CS2 Fall 2024 Note 31

## List comprehension

The syntax is

<pre>
[ <em>expression</em> for <em>variable</em> in <em>sequence</em> if <em>condition</em> ]
</pre>

The `if` portion is optional.

### Examples

Let us assume we have some list of integers, for instance

```
xs = [ 4, 7, 5, 1, 0, 9, 6, 3, 8, 2]
```

Here is a new list of the squares of the elements in `xs`.

```
[ x**2 for x in xs ]
```

Here is a new list with the elements of `xs` that are less than 5.

```
[ x for x in xs if x < 5 ]
```

Here is a list of 5 `True` boolean values.

```
[ True for x in range(5) ]
```

Since the expression doesn't use the variable we can write.

```
[ True for _ in range(5) ]
```

Here is a two-dimensional array of zeros.

```
[ [ 0.0 for _ in range(3)] for _ in range(2) ]
```
