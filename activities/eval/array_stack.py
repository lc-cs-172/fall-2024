""""Implement a stack collection that supports `is_empty`, `push` and `pop`."""

class ArrayStack:

    def __init__(self):
        self.data = [None]
        self.size = 0

    def push(self, item):
        if self.size == len(self.data):
            self.resize(2*self.size)
        self.data[self.size] = item
        self.size += 1

    def pop(self):
        item = self.data[self.size - 1]
        self.data[self.size - 1] = None   # avoid loitering
        self.size -= 1
        if self.size > 0 and self.size == len(self.data)//4:
            self.resize(len(self.data)//2)
        return item

    def is_empty(self):
        return self.size == 0

    def resize(self, new_size):
        new_data = [None]*new_size
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data
