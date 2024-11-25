# CS2 Fall 2024 Note 33

## Stacks

A stack supports the following operations:

* `is_empty` returns `True` if the stack is empty
* `pop` removes and returns the top item from the stack
* `push` adds an item to the top of the stack

### Linked-based implementation

For this implementation we need a basic building block:

```python
class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next
```

This building block represents a node in a linked list.

Using this building block, we can implement the three stack operations as
follows:

```python
class LinkedStack:
    def __init__(self):
        self.top = None

    def push(self, item):
        self_top = Node(item, self.top)

    def pop(self):
        result = self.top.item
        self.top = self.top.next
        return result

    def is_empty(self):
        return self.top is None
```
