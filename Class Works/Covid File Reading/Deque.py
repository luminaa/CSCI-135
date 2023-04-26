class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def append(self, item):
        self.items.append(item)

    def append_left(self, item):
        self.items.insert(0, item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def pop_left(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def __iter__(self):
        return iter(self.items)
    
    def __len__(self):
        return len(self.items)