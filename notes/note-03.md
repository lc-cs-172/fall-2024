# Note 03

## Loops

### The `while` loop

The `while` statement has a very similar syntax to the corresponding statement
found in C or Java and requires the same "ingredients".  Here is a simple code
snippet printing numbers *0* through *n - 1*.

```python
i = 0          # initialization (outside the loop)
while i < n:   # expression guarding the entry to the loop body
    print(i)
    i += 1     # update of the control variable
```

### The `for` loop

The `for` statement in Python is rather different than the `for` statement found
in C in spite of the similar name.  It is similar to the "for each" construct
available in Java.

The `for` loop syntax is as follows:

<pre>
for <em>variable</em> in <em>sequence</em>:
    <em>statement</em>
    ...
</pre>

where *sequence* is an expression evaluating into a sequence of values.

Its flow is:
1. If there are no values in *sequence* that haven't been visited yet, stop.
1. Assign *variable* to the next value in *sequence*.
3. Execute the statements in the body of the loop.
4. Go back to step 1.

Here is a faithful translation of the `while` loop above using `for`:

```python
for i in range(n):
    print(i)
```

For our purpose, `range` behaves like a function that returns a sequence of
numbers based on the given arguments; here numbers *0* to *n - 1*.  Read the
official
[documentation](https://docs.python.org/3/library/functions.html#func-range) to
find out details about this useful "function".

Strings and lists can be used in contexts demanding a sequence (e.g., a `for`
loop).  When a string is used as a sequence, each of the characters of the
string are given out, one at a time.  Similarly, when a list is used as a
sequence, each of its elements are given out, one at a time.

### The `break` and `continue` statements

A `break` statement (just the word `break`) exits the current loop.  If inside
multiple nested loops, `break` only exits the innermost loop.

A `continue` statement skips the rest of the current loop iteration.

## Readings

Please read the following Pythonorama pages by Wednesday:

* https://github.com/alainkaegi/pythonorama/blob/main/control_structures/loops.md
* https://github.com/alainkaegi/pythonorama/blob/main/development_tools/command_line.md
* https://github.com/alainkaegi/pythonorama/blob/main/control_structures/your_first_program.md
* https://github.com/alainkaegi/pythonorama/blob/main/development_tools/vs_code.md
