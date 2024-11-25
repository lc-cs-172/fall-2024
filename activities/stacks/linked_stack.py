""""Implement a stack collection that supports `is_empty`, `push` and `pop`."""

class LinkedStack:
    class Node:
        def __init__(self, item, next):
            self.item = item
            self.next = next

    def __init__(self):
        self._top = None

    def push(self, item):
        self._top = LinkedStack.Node(item, self._top)

    def pop(self):
        result = self._top.item
        self._top = self._top.next
        return result

    def is_empty(self):
        return self._top is None
