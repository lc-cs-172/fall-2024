# CS2 Fall 2024 Note 35

## Stacks (continued)

### Primitive arrays

Primitive arrays support the following operations:

* Allocate an array
* Access a singular element
* Set a singular element to a particular value
* Get the length of an array

To use Python's convenient list syntax while limiting yourself to what a
primitive array can do, use only the following features:

Operation|Syntax
-|-
Allocate an array of length $n$|`a = [None] * n`
Access element $i$|`a[i]`
Set element $i$ to $x$|`a[i] = x`
Get the length of an array|`len(a)`

### Array-based implementation

Let's implement the stack collection using primitive arrays!
