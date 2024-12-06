# CS2 Fall 2024 Note 39

## Searching

Suppose you are given the task to write a function

```
search(haystack : list[int], needle : int) -> int:
```

that searches the array `haystack` for the value `needle`.  It returns either
`-1`, if it cannot find the value or returns the index of the first occurrence
of `needle` in `haystack`.

What is the runtime of `search` as a function of the number of elements in
`haystack`?

Is this the best you can do?

Can you improve the runtime, if the values in `haystack` are in sorted order?
